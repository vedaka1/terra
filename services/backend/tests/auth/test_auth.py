import pytest
from httpx import AsyncClient

from src.users.dao import UserDAO


@pytest.mark.asyncio(scope="session")
class TestAuth:

    async def test_register(self, client: AsyncClient):
        response = await client.post(
            "/auth/register",
            json={
                "email": "test_auth@test.com",
                "username": "test_user_auth",
                "password": "1234qwe",
            },
        )
        assert response.status_code == 201

    async def test_login(self, client: AsyncClient):
        response = await client.post(
            "/auth/login", data={"username": "test_user_auth", "password": "1234qwe"}
        )
        assert response.status_code == 200
        assert response.cookies.get("access_token") is not None

    async def test_refresh_token(self, client: AsyncClient):
        response = await client.post("/auth/refresh")
        assert response.status_code == 200
        assert response.cookies.get("access_token") is not None
        assert response.cookies.get("refresh_token") is not None

    async def test_logout(self, client: AsyncClient):
        response = await client.post("/auth/logout")
        assert response.status_code == 200
        assert response.cookies.get("access_token") is None
        assert response.cookies.get("refresh_token") is None
