##############################################################
# USE THESE LINKS AS REFERENCE FOR MYSQL
##############################################################
# http://flask-mysqldb.readthedocs.io/en/latest/
# http://codehandbook.org/python-web-application-flask-mysql/
# https://community.c9.io/t/setting-up-mysql/1718
##############################################################

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
  data = cursor.fetchone()

  if data is None:
    return "Username or Password is wrong"
  else:
    return "Logged in successfully"


app.run(C9_HOST, C9_PORT)
