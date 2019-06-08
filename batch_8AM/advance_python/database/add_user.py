import pymysql as sql
db = sql.connect(host="localhost",port=3306,database='internshipbatch',user='project',password='password')
c = db.cursor()
while True:
    name = input("Enter your name : ")
    address = input("ENter your address : ")
    course = input("Enter your course : ")
    dob = input("Enter your date of birth : ")
    phno = int(input("Enter your phone number : "))
    cmd = "insert into student(name,address,course,dob,phno) values('{}','{}','{}','{}',{})".format(name,address,course,dob,phno)
    c.execute(cmd)
    print("Data inserted")
    db.commit()
    ch = input("Do you want to continue : ").lower().strip()
    if ch == "no":
        break
