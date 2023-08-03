from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
app=Flask(__name__)

mysql = MySQL(app)

@app.route('/index') 
def index():
    return render_template('index.html')

@app.route('/login') 
@app.route('/login', methods =['GET', 'POST'])
def login():
    return render_template('login.html')

#@app.route('/register') 
@app.route('/register', methods =['POST', 'GET'])
def register():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    success_msg=None
    error=None
    if request.method=='POST':
       firstname= request.form['firstname']
       lastname= request.form['firstname']
       email= request.form['email']
       password=request.form['password']
       password2=request.form['password2']
       if firstname=="" or len(firstname)<2:
          error='Firstname must not be blank and contain at least 3 characters' 
       elif lastname=="" or len(lastname)<2:
          error='lastname must not be blank and contain at least 3 characters' 
       elif not re.fullmatch(regex, email):
             error='invalid email' 
       elif password=="" or len(password)<6:
             error='password must not be blank and contain at least 6 characters' 
             if password!=password2:
                error='password must match' 
       
       else:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            query='INSERT INTO users(id,firstname,lastname,email,password) VALUES (NULL, % s, % s, % s, % s))'
            cursor.execute(query,(firstname,lastname,email,password))
            mysql.connection.commit()
            success_msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
           
    return render_template('register.html',error=error,msg=success_msg)



if __name__=="__main__":
  app.run(debug=True)