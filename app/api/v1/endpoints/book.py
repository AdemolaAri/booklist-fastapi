import json
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from app.database.mock import MockBooks
from app.model.book import Book, BookInDB
from app.service import csv
from typing import List

router = APIRouter(
    tags=['books'],
)


@router.get("/books")
def get_books():
    return {'books': MockBooks}


@router.get("/books/{book_id}")
def get_book(book_id: int):
    book = next((book for book in MockBooks if book.id == book_id), None)
    return {'book': book}


@router.post("/books")
def create_book(book: Book, status_code=status.HTTP_201_CREATED) -> List[BookInDB]:
    id = len(MockBooks) + 1
    new_book = BookInDB(**book.__dict__, id=id)
    MockBooks.append(new_book)
    return MockBooks
