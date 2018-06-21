from flask import Flask, render_template, request
from api import *
from sqlite3 import connect

app = Flask(__name__)
db = 'database.db'


@app.route('/')
def hello():
    return 'hello'


@app.route('/<user>')
def make_order(user):
    return render_template('order.html', name=user)


@app.route('/add_order', methods=['POST', 'GET'])
def add_order():
    return create_order(request)


if __name__ == '__main__':
    app.run(debug=True)
