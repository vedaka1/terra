import pytest
from httpx import AsyncClient


@pytest.fixture(scope="session", autouse=True)
async def client(client: AsyncClient):
    response = await client.post(
        "/auth/register",
        json={
            "email": "test1@test.com",
            "username": "test_user1",
            "password": "1234qwe",
        },
    )
    assert response.status_code == 201
    response = await client.post(
        "/auth/login", data={"username": "test_user1", "password": "1234qwe"}
    )
    assert response.status_code == 200
    yield client
    await client.post("/auth/logout")
