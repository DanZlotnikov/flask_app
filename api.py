from sqlite3 import *
from flask import render_template

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
                msg = "Record successfully added"

        except Exception as e:
            msg = 'Order creation failed: "{}"'.format(e.message)

        finally:
            conn.close()
            return render_template("receipt.html", result=request.form, msg=msg)

