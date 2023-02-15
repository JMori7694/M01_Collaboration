import sqlite3
import random


def getNewId():
    return random.getrandbits(28)


books = [
    {
        'book_name': 'Introducing Python: Modern Computing in Simple Packages: Second Edition',
        'author': 'Lubanovic, Bill',
        'publisher': "O'Reilly"
    },

    {
        'book_name': 'Yookoso! An Invitation to Contemporary Japanese: Third Edition',
        'author': 'Tohsaku, Yasu-Hiko',
        'publisher': 'McGraw Hill'
    },

    {
        'book_name': 'Genki: An Intergrated Course in Elementary Japanese: Volume 1: Second Edition',
        'author': 'Banno, Eri, et. al.',
        'publisher': 'The Japan Times'
    },

    {
        'book_name': 'The Secret History of Twin Peaks',
        'author': 'Frost, Mark',
        'publisher': 'Flatiron Books'
    },

    {
        'book_name': 'Rurouni Kenshin: Restoration: Volume 1',
        'author': 'Watsuki, Nobuhiro',
        'publisher': 'Shonen Jump Manga'
    },

    {
        'book_name': 'Rurouni Kenshin: Restoration: Volume 1',
        'author': 'Watsuki, Nobuhiro',
        'publisher': 'Shonen Jump Manga'
    },

    {
        'book_name': 'Land of the Lustrous: Volume 1',
        'author': 'Ichikawa, Haruko',
        'publisher': 'Kodansha Comics'
    },

    {
        'book_name': 'Land of the Lustrous: Volume 2',
        'author': 'Ichikawa, Haruko',
        'publisher': 'Kodansha Comics'
    }
]


def connect():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, book_name TEXT, author TEXT, publisher TEXT)")
    conn.commit()
    conn.close()
    for i in books:
        bk = (getNewId(), i['book_name'], i['author'], i['publisher'])
        insert(bk)


def insert(book):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO books VALUES (?,?,?,?)", (
        book.id,
        book.book_name,
        book.author,
        book.publisher
    ))
    conn.commit()
    conn.close()


def update(book):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("UPDATE books SET book_name=?, author=?, publisher=? WHERE id=?",
                (book.book_name, book.author, book.publisher, book.id))
    conn.commit()
    conn.close()
