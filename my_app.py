from flask import *
import api

app = Flask(__name__)
db = 'database.db'


@app.route('/')
def blank_url():
    return redirect(url_for('order'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    return api.login(request)


@app.route('/logout')
def logout():
    return api.logout()


@app.route('/homepage')
def homepage():
    return render_template('homepage.html')


@app.route('/order')
def order():
    logged = request.cookies.get('logged')
    email = request.cookies.get('email')
    return render_template('order.html', logged=logged, email=email)


@app.route('/available_requests')
def available_requests():
    logged = request.cookies.get('logged')
    email = request.cookies.get('email')
    industry = request.cookies.get('industry')
    return api.available_requests(logged=logged, email=email, industry=industry)


@app.route('/my_orders')
def my_orders():
    logged = request.cookies.get('logged')
    email = request.cookies.get('email')
    industry = request.cookies.get('industry')
    return api.my_orders(logged=logged, email=email, industry=industry)


@app.route('/add_order', methods=['POST', 'GET'])
def add_order():
    logged = request.cookies.get('logged')
    email = request.cookies.get('email')
    return api.create_order(request, logged, email)


@app.route('/create_new_user')
def create_new_user():
    return render_template('/create_new_user.html')


@app.route('/add_user', methods=['POST', 'GET'])
def add_user():
    return api.add_user(request)


if __name__ == '__main__':
    app.run(debug=True)
