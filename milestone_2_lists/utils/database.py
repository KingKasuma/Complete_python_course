import json
"""
Concerned with storing and retrieving books from a list.
Format of the csv file:

name,author,read\n
"""
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
books_file = 'books.json'


def create_book_table():
    with open(books_file, 'w') as file:
        json.dump([], file)


def add_book(name, author):
    books = get_all_books()
    books.append({'name': name, 'author': author, 'read': False})
    _save_all_books(books)


def get_all_books():
    with open(books_file, 'r') as file:
        return json.load(file)

def  _save_all_books(books):
    with open(books_file, 'w') as file:
        json.dump(books, file)       

def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = True
    _save_all_books(books)

def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)
############ Save into JSON file ############