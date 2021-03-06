from flask import *
import api
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'C:\Users\Dan.Z\Desktop'
ALLOWED_EXTENSIONS = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx']
myapp = Flask(__name__)
myapp.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
myapp.secret_key = 'super secret key'
myapp.config['SESSION_TYPE'] = 'filesystem'

db = 'database.db'


@myapp.route('/')
def blank_url():
    return redirect(url_for('order'))


@myapp.route('/login', methods=['POST', 'GET'])
def login():
    return api.login(request)


@myapp.route('/logout')
def logout():
    return api.logout()


@myapp.route('/homepage')
def homepage():
    return render_template('homepage.html')


@myapp.route('/order')
def order():
    logged = request.cookies.get('logged')
    email = request.cookies.get('email')
    return render_template('order.html', logged=logged, email=email)


@myapp.route('/available_requests')
def available_requests():
    logged = request.cookies.get('logged')
    email = request.cookies.get('email')
    industry = request.cookies.get('industry')
    return api.available_requests(logged=logged, email=email, industry=industry)


@myapp.route('/my_orders')
def my_orders():
    logged = request.cookies.get('logged')
    email = request.cookies.get('email')
    industry = request.cookies.get('industry')
    return api.my_orders(logged=logged, email=email, industry=industry)


@myapp.route('/add_order', methods=['POST', 'GET'])
def add_order():
    logged = request.cookies.get('logged')
    email = request.cookies.get('email')

    return api.create_order(request, logged, email)


@myapp.route('/create_new_user')
def create_new_user():
    return render_template('/create_new_user.html')


@myapp.route('/add_user', methods=['POST', 'GET'])
def add_user():
    return api.add_user(request)


if __name__ == '__main__':
    myapp.run(debug=True)
