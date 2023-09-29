"""The main script for the application"""
from fastapi import FastAPI
from database.db import init_db
from routers.books import books_router

app = FastAPI(
    title="Books App Backend",
    description="Backend for the Books App",
    version="0.1.0"
)


@app.on_event("startup")
async def app_startup():
    """Logic to run on app startup"""
    await init_db()


@app.get("/")
async def root() -> dict[str, str]:
    """The root endpoint of the application"""
    return {"Message": "Why are you gae?"}

app.include_router(books_router)
