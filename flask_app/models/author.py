from flask_app.config.mysqlconnection import MySQLConnection
from flask_app.models import book 
# author.authors_who_favorited.append(book.Book(data))

class Author:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.favorite_books = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorite_books = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        authors = []
        results = MySQLConnection('esquema_libros').query_db(query)
        for row in results:
            authors.append(cls(row))
        return authors

    @classmethod
    def save(cls,data):
        query = "INSERT INTO authors (name) VALUES (%(name)s);"
        return MySQLConnection('esquema_libros').query_db(query,data)

    @classmethod
    def unfavorited_authors(cls,data):
        query = "SELECT * FROM authors WHERE authors.id NOT IN ( SELECT author_id FROM favorites WHERE book_id = %(id)s );"
        authors = []
        results = MySQLConnection('esquema_libros').query_db(query,data)
        for row in results:
            authors.append(cls(row))
        return authors

    @classmethod
    def add_favorite(cls,data):
        query = "INSERT INTO favorites (author_id,book_id) VALUES (%(author_id)s,%(book_id)s);"
        return MySQLConnection('esquema_libros').query_db(query,data)

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON books.id = favorites.book_id WHERE authors.id = %(id)s;"
        results = MySQLConnection('esquema_libros').query_db(query,data)

        # Crea una instancia de autor
        author = cls(results[0])
        # agrega todos los objetos de libro a  la lista de favoritos.
        for row in results:
            # si no hay favoritos
            if row['books.id'] == None:
                break
            data = {
                "id": row['books.id'],
                "title": row['title'],
                "num_of_pages": row['num_of_pages'],
                "created_at": row['books.created_at'],
                "updated_at": row['books.updated_at']
            }
            author.favorite_books.append(book.Book(data))
        return author