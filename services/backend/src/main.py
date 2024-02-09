from typing import List
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from src.users.router import user_router, auth_router


app = FastAPI()


# Allow recieve requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "HEAD", "OPTIONS"],
    allow_headers=["Access-Control-Allow-Headers", 'Content-Type', 'Authorization', 'Access-Control-Allow-Origin'], 
)

app.include_router(user_router)
app.include_router(auth_router)


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <a href="http://localhost:5000/docs">Documentation</a><br>
    <a href="http://localhost:5000/redoc">ReDoc</a>
    """
