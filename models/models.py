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
        name = "books_collection"
