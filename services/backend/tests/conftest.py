import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy import text

from src.config import settings
from src.database import Base, engine
from src.main import app


@pytest.fixture(scope="session", autouse=True)
async def setup_db():
    assert settings.MODE == "TEST"
    async with engine.begin() as conn:
        await conn.execute(text("CREATE SCHEMA IF NOT EXISTS fastapi;"))
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="session")
def client():
    client = AsyncClient(
        base_url="http://localhost:5000", transport=ASGITransport(app=app)
    )
    yield client
