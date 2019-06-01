from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import cofig

app = Flask(__name__)

from SQLTable import Note, init_db

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:jiaoyebaobei080426@localhost:3306/db_name'
db = SQLAlchemy(app)

db.create_all()


@app.route('/')
def hello_world():
    init_db()
    return "<hi>Hello World!</hi>"


@app.route('/shou')
def shouthesql():
    jg = Note.Query.all()
    return '<show>' + jg + '</show>'


@app.route('/add')
def add():
    body = request.args.get('body', cofig.defmsg)
    thecommit = Note(cofig.nextid, body)
    cofig.nextid += 1


app.run()
