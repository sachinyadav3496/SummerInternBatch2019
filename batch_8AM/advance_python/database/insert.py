import sqlite3 as sql

db = sql.connect("student.db")
c = db.cursor()
#cmd = "create table student(name varchar(100),address varchar(50),course varchar(60),phno varchar(15))"
#c.execute(cmd)
while True:
    name = input("Enter your name : ")
    address = input("Enter your address : ")
    course = input("Enter your course : ")
    phno = input("ENter your phone number : ")
    cmd = "insert into student values('{}','{}','{}','{}')".format(name,address,course,phno)
    c.execute(cmd)
    choice = input("Do you want to continue (yes/no) : ")
    if choice.strip().lower() == 'no':
        break
