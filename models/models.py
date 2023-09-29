"""The model file for the data"""
from typing import List, Optional

from beanie import Document
from pydantic import BaseModel


class Book(Document):
    """A template for the Book document"""
    title: str
    author: str
    published_date: int
    reviews: List[str] = []

    class Settings:
        """The class with the settings for the Book class"""
        name = "books_document"

    class Config:
        """The config class for Book"""
        schema_extra = {
            "example": {
                "title": "The Lord of the Rings",
                "author": "J.R.R. Tolkien",
                "published_date": 1954,
                "reviews": [
                    "Great book!",
                    "Very informative!",
                    "Would make for a great movie franchise"
                ]
            }
        }


class UpdateBook(BaseModel):
    """The schema used to update the book"""
    title: Optional[str]
    author: Optional[str]
    published_date: Optional[int]
