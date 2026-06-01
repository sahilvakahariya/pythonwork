import mysql.connector as sql

conn=sql.connect(
    host="localhost",
    user="root",
    password="sahil$0030"
    )

print("Successful")

cursor=conn.cursor()
cursor.execute("create database sahil")
