# create a CRUD API for a Book
# The Book model should have the following parameters:
# id
# book_name
# author
# publisher

from flask import Flask, render_template, request, jsonify
import sqlite3

db = sqlite3.connect('books.db')
cur = db.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Books (
                id INTEGER PRIMARY KEY,
                book_name STRING,
                author STRING,
                publisher STRING)''')
cur.close()

app = Flask(__name__)

if __name__ == '__main__':
    app.run()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/books')
def get_books():
    db = sqlite3.connect('books.db')
    cur = db.cursor()
    books = cur.fetchall()

    output = []
    for bk in books:
        book_data = {'book_name': bk.book_name,
                     'author': bk.author,
                     'publisher': bk.publisher}

        output.append(book_data)
        return {"Books": output}
    cur.close()


@app.route('/books/<id>')
def get_book(id):
    db = sqlite3.connect('books.db')
    cur = db.cursor()
    bk = cur.fetchall(id)
    cur.close()
    return jsonify({'book_name': bk.book_name, 'author': bk.author, 'publisher': bk.publisher})


@app.route('/books', methods=['POST'])
def add_book():
    db = sqlite3.connect('books.db')
    cur = db.cursor()
    bk = Book(
        book_name=request.json['book_name'],
        author=request.json['author'],
        publisher=request.json['publisher'])
    cur.execute('''INSERT INTO Books''',
                bk['book_name'], bk['author'], bk['publisher'])
    db.commit()
    cur.close()
    return {'id': bk.id}


@app.route('/books/<id>', methods=['DELETE'])
def delete_bk(id):
    db = sqlite3.connect('books.db')
    cur = db.cursor()
    bk = cur.fetchall(id)
    if bk is None:
        return {'Error': 'not found'}
    cur.execute('''DELETE FROM Books''', bk)
    db.commit()
    cur.close()
    return {'Goodbye book!'}


Book = {}
# class Book():
#    def __init__(self, book_name, author, publisher):
#        self.book_name = book_name,
#        self.author = author,
#        self.publisher = publisher
#
#    def __repr__(self):
#        return f'{self.book_name} - {self.author} - {self.publisher}'
