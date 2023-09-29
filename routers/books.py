"""The Books Route Logic"""
from fastapi import APIRouter, FastAPI, HTTPException, status

from models.models import Book

books_router = APIRouter(prefix="/books", tags=["Books"])


@books_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=Book
)
async def create_book(book: Book):
    """Create a new book"""
    await book.insert()
    return book
