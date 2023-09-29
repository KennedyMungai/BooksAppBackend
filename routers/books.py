"""The Books Route Logic"""
from typing import List
from fastapi import APIRouter, FastAPI, HTTPException, status
from beanie import PydanticObjectId

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


@books_router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[Book]
)
async def retrieve_all_books() -> List[Book]:
    """The endpoint to retrieve all the books in the database

    Returns:
        List[Book]: The list of all the books in the database
    """
    books = await Book.find_all().to_list()
    return books


@books_router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=Book
)
async def retrieve_book_by_id(id: PydanticObjectId) -> Book:
    """The endpoint to retrieve a book by its i

    Args:
        id (PydanticObjectId): The type of value if the mongodb id

    Raises:
        HTTPException: A 404 is raised if the book is not found

    Returns:
        Book: The book whose id is the argument
    """
    book = await Book.get(id)

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book
