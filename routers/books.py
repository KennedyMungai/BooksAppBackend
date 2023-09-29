"""The Books Route Logic"""
from typing import List

from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, status

from models.models import Book, UpdateBook
from utils.utilities import encode_input

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
    "/{_id}",
    status_code=status.HTTP_200_OK,
    response_model=Book
)
async def retrieve_book_by_id(_id: PydanticObjectId) -> Book:
    """The endpoint to retrieve a book by its i

    Args:
        id (PydanticObjectId): The type of value if the mongodb id

    Raises:
        HTTPException: A 404 is raised if the book is not found

    Returns:
        Book: The book whose id is the argument
    """
    book = await Book.get(_id)

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book


@books_router.put(
    "/{_id}",
    status_code=status.HTTP_200_OK,
    response_model=Book
)
async def update_book(_id: PydanticObjectId, book_data: UpdateBook):
    """The function endpoint for updating books

    Args:
        _id (PydanticObjectId): The id of the book being updated
        book_data (UpdateBook): The data used to update the book

    Raises:
        HTTPException: A 404 is raised if the book is not found

    Returns:
        Book: The updated book
    """
    book = await Book.get(_id)

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The book was not found"
        )

    book_data = encode_input(book_data)
    _ = await book.update(**book_data)

    updated_book = await Book.get(_id)

    return updated_book


@books_router.delete("/{_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_single_book(_id: PydanticObjectId) -> None:
    """The endpoint to delete a single book

    Args:
        _id (PydanticObjectModel): The id of the book to be deleted 

    Raises:
        HTTPException: A 404 is raised of the book os not found

    Returns:
        None: Returns nothing
    """
    book = await Book.get(_id)

    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="The book was not found")

    await book.delete()

    return None
