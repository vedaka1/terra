from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from sqlalchemy import text
from src.chats.router import chat_router
from src.database import Base, engine
from src.users.router import auth_router, user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.execute(text("CREATE SCHEMA IF NOT EXISTS fastapi;"))
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)


# Allow recieve requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8080",
        "http://localhost:80",
        "http://176.109.106.9:8080",
        "http://176.109.106.9:80",
        "http://172.29.24.31:8080",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "HEAD", "OPTIONS", "DELETE"],
    allow_headers=[
        "Access-Control-Allow-Headers",
        "Content-Type",
        "Authorization",
        "Access-Control-Allow-Origin",
    ],
)

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(chat_router)


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <a href="http://localhost:5000/docs">Documentation</a><br>
    <a href="http://localhost:5000/redoc">ReDoc</a>
    """
