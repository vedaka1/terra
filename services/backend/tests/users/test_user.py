import pytest
from httpx import AsyncClient


@pytest.mark.asyncio(scope='session')
class TestUser:
    
    async def test_get_user_profile(self, client: AsyncClient):
        response = await client.get('/users/me')
        assert response.status_code == 200

    async def test_get_all_users(self, client: AsyncClient):
        response = await client.get('/users/all')
        assert isinstance(response.json(), list)
        assert response.status_code == 200

    async def test_add_friend(self, client: AsyncClient):
        data = {'email': 'test3@test.com', 'username': 'test_user3', 'password': '1234qwe'}
        response = await client.post(
            '/auth/register',
            json=data
            )
        assert response.status_code == 201
        new_user = response.json()
        response = await client.post(
            '/users/me/friend',
            params={'friend_id': new_user['id']}
            )
        assert response.status_code == 200

    async def test_get_all_user_friends(self, client: AsyncClient):
        response = await client.get('/users/me/friends')
        assert isinstance(response.json(), list)
        assert response.status_code == 200

    async def test_delete_user_friend(self, client: AsyncClient):
        response = await client.get('/users/me/friends')
        assert response.status_code == 200
        friend = response.json()[0]
        response = await client.delete(
            '/users/me/friend',
            params={'friend_id': friend['id']}
            )
        assert response.status_code == 200