import os
from flask import Flask, request
from flask_mysqldb import MySQL

C9_HOST = os.getenv('IP', '0.0.0.0')
C9_PORT = int(os.getenv('PORT', 8080))

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'EmpData'
app.config['MYSQL_DATABASE_HOST'] = C9_HOST
mysql.init_app(app)


@app.route("/")
def hello():
  return "Welcome to Python Flask App!"


@app.route("/Authenticate")
def Authenticate():
  username = request.args.get('UserName')
  password = request.args.get('Password')
  cursor = mysql.connection.cursor()
  cursor.execute("SELECT * from User where Username='" + username +
                 "' and Password='" + password + "'")
  rv = cursor.fetchall()
  return str(username)


app.run(C9_HOST, C9_PORT)
