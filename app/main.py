"""The main script for the application"""
from fastapi import FastAPI


app = FastAPI(
    title="Books App Backend",
    description="Backend for the Books App",
    version="0.1.0"
)


@app.get("/")
async def root() -> dict[str, str]:
    return {"Message": "Why are you gae?"}
