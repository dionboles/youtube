from flask import Flask,render_template,request,redirect,url_for
import MySQLdb

app = Flask(__name__)

conn = MySQLdb.connect(host="localhost",user="root",password="",db="login_data")

@app.route("/")
def index():
	return render_template("index.html", title="SignUP")



@app.route("/signUp",methods=["POST"])
def signUp():
	username = str(request.form["user"])
	password = str(request.form["password"])
	email = str(request.form["email"])
	
	cursor = conn.cursor()
	
	cursor.execute("INSERT INTO user (name,password,email)VALUES(%s,%s,%s)",(username,password,email))
	conn.commit()
	return redirect(url_for("login"))
	

@app.route("/login")
def login():
	return render_template("login.html",title="data")

@app.route("/checkUser",methods=["POST"])
def check():
	username = str(request.form["user"])
	password = str(request.form["password"])
	cursor = conn.cursor()
	cursor.execute("SELECT name FROM user WHERE name ='"+username+"'")
	user = cursor.fetchone()
	
	if len(user) is 1:
		return redirect(url_for("home"))
	else:
		return "failed"
@app.route("/home")
def home():
	return render_template("home.html")
if __name__ == "__main__":
	app.run(debug=True)