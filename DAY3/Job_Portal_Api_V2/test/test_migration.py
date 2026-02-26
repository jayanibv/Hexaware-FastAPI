import os
import sys
import pytest
from sqlalchemy import inspect, text
from alembic.config import Config
from alembic import command

# Add the project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine
from app.database.base import Base

# Use a dedicated SQLite engine for migration tests
TEST_SQLALCHEMY_DATABASE_URL = "sqlite:///./alembic_test.db"
test_engine = create_engine(TEST_SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

@pytest.fixture(autouse=True)
def clean_db():
    """Ensure a clean database before each test."""
    Base.metadata.drop_all(bind=test_engine)
    # Also drop alembic_version if it exists
    with test_engine.connect() as conn:
        conn.execute(text("DROP TABLE IF EXISTS alembic_version"))
        conn.commit()
    yield
    Base.metadata.drop_all(bind=test_engine)

def test_database_tables(clean_db):
    """Verify that all expected tables are created in the database."""
    # Ensure tables are created via Base.metadata
    Base.metadata.create_all(bind=test_engine)
    
    inspector = inspect(test_engine)
    tables = inspector.get_table_names()
    
    expected_tables = ["users", "companies", "jobs", "applications"]
    for table in expected_tables:
        assert table in tables, f"Table {table} not found in database"
    
    # Verify specific columns
    user_columns = [col["name"] for col in inspector.get_columns("users")]
    assert "id" in user_columns
    assert "email" in user_columns

def test_run_alembic_migrations():
    """Verify that Alembic migrations can be applied successfully."""
    # Force alembic to use the same database as the engine we are inspecting
    alembic_cfg = Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", str(test_engine.url))
    
    # Run the migration
    try:
        command.upgrade(alembic_cfg, "head")
    except Exception as e:
        pytest.fail(f"Alembic upgrade failed: {e}")
    
    inspector = inspect(test_engine)
    tables = inspector.get_table_names()
    
    # Check for alembic_version table
    assert "alembic_version" in tables, f"alembic_version table not found in {tables}"
    
    # Check that our models were created
    assert "users" in tables
    assert "jobs" in tables
