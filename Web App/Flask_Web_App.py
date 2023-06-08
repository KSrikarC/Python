import os
os.system('cmd /c cls')


from flask import Flask , render_template
from sql_methods import *
app = Flask(__name__)

@app.route('/')
def index():
    records = fetch_records(start_connection())
    return render_template("index.html",records=records)




if __name__ == '__main__':
    app.run()