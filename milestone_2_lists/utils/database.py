#import json
#import sqlite3
from typing import List, Dict, Union
from .database_connection import DatabaseConnection
"""
Concerned with storing and retrieving books from a list.
Format of the csv file:

name,author,read\n
"""

Book = Dict(str, Union(str, int)) #a new Type created
############ Save into CSV file ############
#books_file = 'books.txt'


#def create_book_table():
#    with open(books_file, 'w') as file:
#        pass # just to make the file is there


#def add_book(name, author):
#    with open('books.txt', 'a') as file:
#        file.write(f'{name},{author},0')


#def get_all_books():
#    with open(books_file, 'r') as file:
#        lines = [line.strip().split(',') for line in file.readlines()]

#    return [
#        {'name': line[0], 'author': line[1], 'read': line[2]}
#        for line in lines
#    ]

#def mark_book_as_read(name):
#    books = get_all_books()
#    for book in books:
#        if book['name'] == name:
#            book['read'] = '1'
#    _save_all_books(books)

#def  _save_all_books(books):
#    with open(books_file, 'w') as file:
#        for book in books:
#            file.write(f"{book['name']},{book['author']},{book['read']}\n")

#def delete_book(name):
#    books = get_all_books()
#    books = [book for book in books if book['name'] != name]
#    _save_all_books(books)

#def delete_book(name):
#    for book in books:
#        if book['name'] == name:
#            books.remove(book)

############ Save into CSV file ############

############ Save into JSON file ############
#books_file = 'books.json'


#def create_book_table():
#    with open(books_file, 'w') as file:
#        json.dump([], file)


#def add_book(name, author):
#    books = get_all_books()
#    books.append({'name': name, 'author': author, 'read': False})
#    _save_all_books(books)


#def get_all_books():
#    with open(books_file, 'r') as file:
#        return json.load(file)

#def  _save_all_books(books):
#    with open(books_file, 'w') as file:
#        json.dump(books, file)

#def mark_book_as_read(name):
#    books = get_all_books()
#    for book in books:
#        if book['name'] == name:
#            book['read'] = True
#    _save_all_books(books)

#def delete_book(name):
#    books = get_all_books()
#    books = [book for book in books if book['name'] != name]
#    _save_all_books(books)
############ Save into JSON file ############

############ Save into SQLITE3 ############
def create_book_table() -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')




def add_book(name: str, author: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'INSERT INTO books VALUES(?,?, 0)', (name, author))




def get_all_books() -> List[Book]:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()] #[{name, author, read},(name, author, read)]
    return books

def mark_book_as_read(name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))

def delete_book(name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE from books WHERE name=?', (name,))

############ Save into SQLITE3 ############