import os
import sys
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

# Add the project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app
from app.database.base import Base
from app.database.session import get_db
from app.core.security import create_access_token
from app.models.user import User
from app.models.job import Job
from app.models.company import Company

# Use in-memory SQLite for testing to avoid locking issues
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def db():
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture
def client(db):
    def override_get_db():
        try:
            yield db
        finally:
            pass
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    del app.dependency_overrides[get_db]

@pytest.fixture
def candidate_token(db):
    user = User(username="candidate_test", email="candidate@test.com", password="hashed_password", role="candidate")
    db.add(user)
    db.commit()
    db.refresh(user)
    return create_access_token({"sub": user.email, "role": user.role, "user_id": user.id})

def test_get_jobs(client, candidate_token):
    response = client.get(
        "/candidate/jobs",
        params={"page": 1, "size": 10},
        headers={"Authorization": f"Bearer {candidate_token}"}
    )
    assert response.status_code == 200
    assert "items" in response.json()

def test_apply_job_not_found(client, candidate_token):
    response = client.post(
        "/candidate/apply/999",
        headers={"Authorization": f"Bearer {candidate_token}"}
    )
    assert response.status_code == 404

def test_apply_job_success(client, db, candidate_token):
    # Setup: Create a company and a job
    company = Company(name="Test Co", description="...")
    db.add(company)
    db.commit()
    job = Job(title="Test Job", description="...", salary=1, company_id=company.id, created_by=1)
    db.add(job)
    db.commit()
    
    response = client.post(
        f"/candidate/apply/{job.id}",
        headers={"Authorization": f"Bearer {candidate_token}"}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "applied"

def test_my_applications(client, candidate_token):
    response = client.get(
        "/candidate/applications",
        params={"page": 1, "size": 10},
        headers={"Authorization": f"Bearer {candidate_token}"}
    )
    assert response.status_code == 200
    assert "items" in response.json()

