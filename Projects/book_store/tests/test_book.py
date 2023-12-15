from lib.book import *

def test_book_construct():
    book = Book(1, "random book", "random author")
    assert book.id == 1
    assert book.title == "random book"
    assert book.author_name == "random author"

def test_book_equal():
    book1 = Book(1, "random book", "random author")
    book2 = Book(1, "random book", "random author")
    assert book1 == book2

def test_book_format():
    book = Book(1, "random book", "random author")
    assert str(book) == 'Book(1, random book, random author)'