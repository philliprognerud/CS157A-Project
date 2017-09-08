import os
from flask import Flask, request
from flask_mysqldb import MySQL

C9_HOST = os.getenv('IP', '0.0.0.0')
C9_PORT = int(os.getenv('PORT', 8080))

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQLE_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'EmpData'
app.config['MYSQL_HOST'] = str(C9_HOST)
app.config['MYSQL_PORT'] = 3306
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
