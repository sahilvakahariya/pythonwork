#  Write a Python program to connect to an SQLite3 database, create a table, insert data, and fetch data. 
import sqlite3
conn = sqlite3.connect("student.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Student(id INTEGER, name TEXT)")
cursor.execute("INSERT INTO Student VALUES(1, 'Sahil')")
conn.commit()
cursor.execute("SELECT * FROM Student")
rows = cursor.fetchall()

for row in rows:
    print(row)
conn.close()