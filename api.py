from sqlite3 import *
from flask import *

db = 'database.db'


def create_order(request):
    if request.method == 'POST':
        msg = "hi"
        try:
            consumer = str(request.form['email'])
            industry = str(request.form['industry'])
            description = str(request.form['description'])

            with connect("database.db") as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO orders  (consumer, industry, description) VALUES (?,?,?)", (consumer, industry, description))

                conn.commit()
                msg = "Order successfully created"

        except Exception as e:
            msg = 'Order creation failed: "{}"'.format(e.message)

        finally:
            conn.close()
            return render_template("receipt.html", result=request.form, msg=msg)


def login(request):
    error = None
    if request.method == 'POST':
        valid_credentials = False
        with connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT password FROM suppliers WHERE email = ?', (request.form['email'],))

            # Search for password in db
            for datarow in cursor.fetchall():
                if str(datarow[0]) == str(request.form['password']):
                    valid_credentials = True

            error = None if valid_credentials else 'Invalid Credentials. Please try again.'

            if valid_credentials:
                redirect_to_index = redirect('/my_orders')
                response = current_app.make_response(redirect_to_index)
                response.set_cookie('logged', value='true')
                response.set_cookie('email', value=request.form['email'])

                cursor.execute('SELECT industry FROM suppliers WHERE email = ?', (request.form['email'],))
                datarow = cursor.fetchone()
                response.set_cookie('industry', str(datarow[0]))

                return response

    return render_template('login.html', error=error)


def logout():
    redirect_to_index = redirect('/order')
    response = current_app.make_response(redirect_to_index)
    response.set_cookie('logged', value='false')
    return response


def add_user(request):
    if request.method == 'POST':
        msg = "hi"
        try:
            email = str(request.form['email'])
            industry = str(request.form['industry'])
            password = str(request.form['password'])

            with connect("database.db") as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO suppliers (email, industry, password) VALUES (?,?,?)", (email, industry, password))

                conn.commit()
                msg = "User successfully created"

        except Exception as e:
            msg = 'User creation failed: "{}"'.format(e.message)

        finally:
            conn.close()
            return render_template("receipt.html", result=request.form, msg=msg)


def my_orders(logged, email, industry):
    with connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, consumer, description FROM orders WHERE industry = ?', (industry,) )

        orders = cursor.fetchall()
        return render_template('my_orders.html', orders=orders, logged=logged, email=email)
