import sqlite3
conn=sqlite3.connect("sahil.db")

q="create table student(id int primary key,name varchar(20),age int)"

q="insert into student values(1,'sahill',10)"
q="insert into student values(2,'sahil khan',21)"
q="insert into student values(3,'ramesh khan',20)"


q="update student set name='sahil khan' where id=1"

q="delete from student where id=3"


conn.execute(q)
conn.commit()

query = " select * from student"
k = conn.execute(query).fetchall()
for i in k:
    print(i)

