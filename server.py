from flask import Flask

app = Flask(__name__)

app.route("/", method = ['POST', 'GET'])
def home():
    return