
from flask import Flask
from birdseye import eye

app = Flask(__name__)

@eye
@app.route("/")

def Initiate():
    name = "Srikar"
    return f'Hi {name}, Welcome to this webpage. Hope you are doing great !!'

if __name__ == '__main__':
    app.run()

