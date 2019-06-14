from flask import Flask,render_template,request
import pymysql as sql
app = Flask(__name__)

@app.route("/")
def index():
    #return "<h1 style='color:red;font-size:50px;'>hello world</h1>"
    return render_template("header.html")

@app.route("/hello/")
def hey():
    return render_template("hello.html",user="simran")

@app.route('/home/')
def home():
    dict = {
        'name' : 'simran',
        'course' : 'python',
        'fees' : 15000,
    }
    return render_template('hello.html',data=dict)

@app.route('/login/',methods=['GET','POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('pass')
    try:
        db = sql.connect(host='localhost',port=3306,database='internshipbatch',user='root',password='')
        c = db.cursor()
        cmd = "select * from users where email='{}'".format(email)
        c.execute(cmd)
        data = c.fetchone()
        print(data)
        if data:
            if data[2]  == password:
                return "<h1 style='color:red'>Welcome user with email {} and password {}".format(email,password)
            else:
                error = "PASSWORD DOES NOT MATCH...TRY AGAIN.."
                return render_template("header.html",error=error)
        else:
            error = "No such user...signup to login"
            return render_template("signup.html",error=error)
    except Exception as e:
        return "ERROR...{}".format(e)

@app.route('/signup/')
def signup():
    return render_template('signup.html')

@app.route('/signup1/',methods=['GET','POST'])
def signup1():
    password = request.form.get('pass')
    cpass = request.form.get('cpass')
    if password == cpass:
        try:
            db = sql.connect(host='localhost',port=3306,user='root',password='',database='internshipbatch')
            c = db.cursor()
            
            email = request.form.get('email')
            username = request.form.get('email')
            profile = request.form.get('myfile')
            cmd = f"insert into users values('{email}','{username}','{password}','{profile}')"
            c.execute(cmd)
            db.commit()

        
            dict = {
            'email' : request.form.get('email'),
            'username' : request.form.get('email'),
            'profile' : request.form.get('myfile'),
            }
            return render_template("hello.html",data=dict)
        except Exception as e:
            return "ERROR...{}".format(e)

    else:
        error = "PASSWORD DOES NOT MATCH...TRY AGAIN"
        return render_template("signup.html",error=error)

if __name__ == "__main__":
    app.run(host="localhost",port=80,debug=True)