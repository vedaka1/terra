import pytest
from httpx import AsyncClient


@pytest.mark.asyncio(scope="session")
class TestChats:

    async def test_create_chat(self, client: AsyncClient):
        response = await client.post("/chats", params={"name": "test"})
        assert response.status_code == 200
        assert response.json()["name"] == "test"

    async def test_get_user_chats_list(self, client: AsyncClient):
        response = await client.get("/chats")
        assert isinstance(response.json(), list)
        for data in response.json():
            assert isinstance(data, dict)
        assert response.status_code == 200

    async def test_send_message(self, client: AsyncClient):
        response = await client.post(
            f"/chats/{1}/messages", params={"content": "Привет!"}
        )
        assert response.status_code == 200
        assert response.json()["content"] == "Привет!"

    async def test_get_chat_messages(self, client: AsyncClient):
        response = await client.post(
            f"/chats/{1}/messages", params={"content": "Привет!"}
        )
        assert response.status_code == 200
        response = await client.get("/chats/1/messages")
        assert isinstance(response.json(), list)
        for data in response.json():
            assert data["content"] == "Привет!"
            assert isinstance(data, dict)
        assert response.status_code == 200

    async def test_delete_chat(self, client: AsyncClient):
        response = await client.delete("/chats/1")
        assert response.status_code == 200
        assert response.json() == None
