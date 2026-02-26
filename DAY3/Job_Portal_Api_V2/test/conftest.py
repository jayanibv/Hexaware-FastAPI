import os
import sys
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

# Ensure the project root is in sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app
from app.database.base import Base
from app.database.session import get_db
from app.core.security import create_access_token
from app.models.user import User

# Use in-memory SQLite for testing to avoid locking and persistence issues
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    """Create database tables once for the entire session."""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def db():
    """Provide a transactional database session for each test."""
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    
    yield session
    
    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture
def client(db):
    """Provide a TestClient with overridden dependencies."""
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
    """Fixture to provide a JWT token for an admin user."""
    user = User(username="admin_global", email="admin_global@test.com", password="hashed_password", role="admin")
    db.add(user)
    db.commit()
    db.refresh(user)
    return create_access_token({"sub": user.email, "role": user.role, "user_id": user.id})

@pytest.fixture
def employer_token(db):
    """Fixture to provide a JWT token for an employer user."""
    user = User(username="employer_global", email="employer_global@test.com", password="hashed_password", role="employer")
    db.add(user)
    db.commit()
    db.refresh(user)
    return create_access_token({"sub": user.email, "role": user.role, "user_id": user.id})

@pytest.fixture
def candidate_token(db):
    """Fixture to provide a JWT token for a candidate user."""
    user = User(username="candidate_global", email="candidate_global@test.com", password="hashed_password", role="candidate")
    db.add(user)
    db.commit()
    db.refresh(user)
    return create_access_token({"sub": user.email, "role": user.role, "user_id": user.id})
