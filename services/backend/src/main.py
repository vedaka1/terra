from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from src.chats.router import chat_router
from src.users.router import auth_router, user_router

app = FastAPI()


# Allow recieve requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://176.109.106.9:8080"],
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
