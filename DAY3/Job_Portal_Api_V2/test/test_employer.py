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
def admin_token(db):
    user = User(username="admin_test", email="admin@test.com", password="hashed_password", role="admin")
    db.add(user)
    db.commit()
    db.refresh(user)
    return create_access_token({"sub": user.email, "role": user.role, "user_id": user.id})

@pytest.fixture
def employer_token(db):
    user = User(username="employer_test", email="employer@test.com", password="hashed_password", role="employer")
    db.add(user)
    db.commit()
    db.refresh(user)
    return create_access_token({"sub": user.email, "role": user.role, "user_id": user.id})

def test_create_job(client, admin_token, employer_token):
    # First need a company (admin required)
    client.post(
        "/admin/companies",
        json={"name": "Employer Company", "description": "Desc"},
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    
    response = client.post(
        "/employer/jobs",
        json={
            "title": "Software Engineer",
            "description": "Full stack",
            "salary": 100000,
            "company_id": 1
        },
        headers={"Authorization": f"Bearer {employer_token}"}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Software Engineer"

def test_update_job(client, db, employer_token):
    # Create a job first
    job = Job(title="Old Title", description="desc", salary=10, company_id=1, created_by=1)
    db.add(job)
    db.commit()
    
    response = client.put(
        f"/employer/jobs/{job.id}",
        json={
            "title": "Senior Software Engineer",
            "description": "Updated desc",
            "salary": 150000,
            "company_id": 1
        },
        headers={"Authorization": f"Bearer {employer_token}"}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Senior Software Engineer"

def test_delete_job(client, db, employer_token):
    # Create a job first
    job = Job(title="Delete Target", description="desc", salary=10, company_id=1, created_by=1)
    db.add(job)
    db.commit()
    
    response = client.delete(
        f"/employer/jobs/{job.id}",
        headers={"Authorization": f"Bearer {employer_token}"}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Job deleted successfully"

def test_applications(client, employer_token):
    response = client.get(
        "/employer/applications",
        params={"page": 1, "size": 10},
        headers={"Authorization": f"Bearer {employer_token}"}
    )
    assert response.status_code == 200
    assert "items" in response.json()

