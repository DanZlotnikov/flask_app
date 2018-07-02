import sqlite3

conn = sqlite3.connect('database.db')
print "Opened database successfully"

conn.execute('INSERT INTO suppliers (email, password, industry) VALUES ("dan@z.com", "123", "Electric");')
print "Table created successfully"
conn.close()
