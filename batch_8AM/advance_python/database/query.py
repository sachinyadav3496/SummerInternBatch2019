import sqlite3 as sql
db = sql.connect("student.db")
c = db.cursor()
cmd = "select * from student1"
c.execute(cmd)
data = c.fetchall()
print(data)
for var in data:
    print("Name : ",var[0])
    print("Address : ",var[1])
    print("Course : ",var[2])
    print("Phone Number : ",var[3])
