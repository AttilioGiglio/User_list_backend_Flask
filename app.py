from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)

@app.route('/', methods=['POST'])
def index():
    return "<h1>HELLO WORLD</h1>"

@app.route('/users', methods=['GET'])
def getusers():
    return 'sucess'

@app.route('/users/<id>', methods=['GET'])
def getuser():
    return 'sucess'

@app.route('/users/<id>', methods=['DELETE'])
def deleteuser():
    return 'sucess'

@app.route('/users/<id>', methods=['PUT'])
def updateuser():
    return 'sucess'

if __name__ == "__main__":
    # Run the app with flask on your pc, port 5000 and also It will give you debugging advice on terminal.
    app.run(host='127.0.0.1', port=4000, debug=True)
