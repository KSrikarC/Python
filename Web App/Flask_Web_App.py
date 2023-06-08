import os
os.system('cmd /c cls')
import mysql.connector
connection = mysql.connector.connect(host='localhost',
                                            database='c361cohort',
                                            user='root',
                                            password='root')
cursor = connection.cursor()                                            

from flask import Flask , render_template, request, redirect, url_for
from sql_methods import *
app = Flask(__name__)

@app.route('/')

def index():
    query = 'SELECT * FROM PYTHON_DB ORDER BY ID'
    cursor.execute(query)
    records = cursor.fetchall()    
    return render_template("index.html",records=records)

@app.route('/insert',methods = ['GET','POST'])
def insert_page():
    if request.method == 'POST':
        ID = request.form['ID']
        name = request.form['Name']
        Dept = request.form['Dept']
        rec = (ID,name,Dept)
        cursor.execute("INSERT INTO PYTHON_DB VALUES (%s,%s,%s)",rec)
        connection.commit()   
        return redirect(url_for('index'))
    return render_template('insert.html')




if __name__ == '__main__':
    app.run()