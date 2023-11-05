import asyncio

from crud.user import create_user, get_user
user = {"user_id": 235222222, "username": "test2", "echo_mode": True}

async def test():
    await get_user(4)
    await create_user(user)
    
asyncio.run(test())