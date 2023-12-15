from lib.book import *

class BookRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM books')
        books = []
        for row in rows:
            items = Book(row["id"], row["title"], row["author_name"])
            books.append(items)
        return books

    def find(self, id):
        rows = self._connection.execute('SELECT * FROM books WHERE id = %s', [id])
        row = rows[0]
        return Book(row['id'], row['title'], row['author_name'])
    
    def create(self, book):
        self._connection.execute('INSERT INTO books (id, title, author_name) VALUES(%s, %s, %s)', [book.id, book.title, book.author_name])
        return None
    
    def delete(self, id):
        self._connection.execute('DELETE FROM books WHERE id = %s', [id])
        return None


    