import sqlite3
conn=sqlite3.connect('database.db')
print ("Database open Successfully")
conn.execute('CREATE TABLE students(name TEXT,addr TEXT,city TEXT,pin TEXT)')
print ("Table Created Successfully")
conn.close()