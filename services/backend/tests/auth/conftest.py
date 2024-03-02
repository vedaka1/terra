import asyncio

import pytest
from httpx import ASGITransport, AsyncClient

from src.main import app

# @pytest.fixture(scope="session", autouse=True)
# def event_loop():
#     loop = asyncio.get_event_loop()
#     print("FFFFFFFFFFFFF")
#     yield loop
#     loop.close()


@pytest.fixture(scope="session")
def client(client: AsyncClient):
    yield client
