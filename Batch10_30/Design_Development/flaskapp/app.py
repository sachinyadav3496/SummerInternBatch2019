from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return """Hello world
    <a href='/form/'>FORM</a>"""

@app.route("/home/<user>")
def home(user):
    return "<h1 style='color:red'>Welcome to my first page {}</h1>".format(user)

@app.route("/form/")
def hello():
    return render_template("form.html")

if __name__ == "__main__":
    app.run(host="localhost",port=80,debug=True)