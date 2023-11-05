from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import users


app = FastAPI()


# Allow recieve requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
