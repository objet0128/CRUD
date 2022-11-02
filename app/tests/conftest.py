from typing import Generator

import pytest
from fastapi.testclient import TestClient

from app.db.init_db import drop_db, init_db
from app.db.session import SessionLocal
from app.main import app


@pytest.fixture()
def test_db() -> Generator:
    """
    this is for set up , and tear down a database
    create all tables before each test, and drop them again afterwards
    """
    init_db()
    yield
    drop_db()


@pytest.fixture(scope="session")
def db() -> Generator:
    yield SessionLocal()


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
