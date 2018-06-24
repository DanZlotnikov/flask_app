from flask import *
import api

app = Flask(__name__)
db = 'database.db'


@app.route('/')
def blank_url():
    return redirect(url_for('login'))


@app.route('/homepage')
def homepage():
    return render_template('homepage.html')


@app.route('/order')
def order():
    return render_template('order.html')


@app.route('/add_order', methods=['POST', 'GET'])
def add_order():
    return api.create_order(request)


@app.route('/create_new_user')
def create_new_user():
    return render_template('/create_new_user.html')


@app.route('/add_user', methods=['POST', 'GET'])
def add_user():
    return api.add_user(request)


@app.route('/login', methods=['POST', 'GET'])
def login():
    return api.login(request)


if __name__ == '__main__':
    app.run(debug=True)
