from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    #return "<h1 style='color:red;font-size:50px;'>hello world</h1>"
    return render_template("header.html")

@app.route("/hello/")
def hey():
    return render_template("hello.html",user="simran")

if __name__ == "__main__":
    app.run(host="localhost",port=80,debug=True)