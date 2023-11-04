from fastapi import APIRouter
from ....database.mock import MockBooks
from booklist.model.book import Book

router = APIRouter(
    tags=['books'],
)

@router.get("/books")
def get_books():
    books = [Book(**book.__dict__) for book in MockBooks]
    return {'books': books}

@router.get("/books/{book_id}")
def get_book(book_id: int):
    book = [book for book in MockBooks if book.id == book_id][0]
    return {'book': book}

@router.post("/books")
def create_book(book: Book):
    books = [Book(**book.__dict__) for book in MockBooks]
    books.append(book)
    return {'books': books}
