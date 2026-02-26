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

def test_create_company(client, admin_token):
    response = client.post(
        "/admin/companies",
        json={"name": "Hexaware", "description": "IT company"},
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Hexaware"

def test_get_all_companies(client, admin_token):
    response = client.get(
        "/admin/companies",
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_all_jobs(client, admin_token):
    response = client.get(
        "/admin/jobs",
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert response.status_code == 200
    assert "items" in response.json()

def test_delete_jobs(client, db, admin_token):
    # Create job via helper to ensure it exists
    job = Job(title="Delete Me", description="...", salary=1, company_id=1, created_by=1)
    db.add(job)
    db.commit()
    
    response = client.delete(
        f"/admin/jobs/{job.id}",
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Job deleted successfully"

def test_all_applications(client, admin_token):
    response = client.get(
        "/admin/applications",
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert response.status_code == 200
    assert "items" in response.json()

