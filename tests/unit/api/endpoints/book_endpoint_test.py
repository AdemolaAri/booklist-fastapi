from app.api.v1.endpoints import book
from app.database.mock import MockBooks
from app.model.book import Book


class TestBookEndPoint:
    def test_get_books(self):
        assert book.get_books() == {'books': MockBooks}

    def test_get_book(self):
        assert book.get_book(1) == {'book': MockBooks[0]}

    def test_create_book(self):
        tempDB = MockBooks[:]
        book.create_book(Book(
            **{'title': 'test', 'author': 'test', 'year_of_publication': 2021, 'review': None}))
        assert len(MockBooks) == len(tempDB) + 1
        assert MockBooks[-1].title == 'test'
        assert MockBooks[-1].author == 'test'
