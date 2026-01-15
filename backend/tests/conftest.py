import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import app
from db.models import Base
from db.session import get_db

# Use a separate test database, same container
TEST_DATABASE_URL = "postgresql://habot:habot@localhost:5432/habot_test_db"

engine = create_engine(TEST_DATABASE_URL)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

# Create tables
Base.metadata.create_all(bind=engine)

# This function replaces the real get_db dependency during tests.
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

# Spins up the FastAPI app in test mode
@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c
