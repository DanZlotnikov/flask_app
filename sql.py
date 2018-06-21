import sqlite3

conn = sqlite3.connect('database.db')
print "Opened database successfully"

conn.execute('CREATE TABLE orders (id integer PRIMARY KEY, consumer text, supplier text, industry text, description text')
print "Table created successfully"
conn.close()
