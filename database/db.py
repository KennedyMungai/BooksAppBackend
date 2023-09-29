"""The database config file"""
from beanie import init_beanie
import motor.motor_asyncio
from models.models import Book


async def init_db():
    """The function that initializes the database"""
    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb://localhost:27017")
    await init_beanie(
        database=client.books_database,
        document_models=[Book],
    )
