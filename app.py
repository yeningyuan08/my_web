from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

from SQLTable import Note,init_db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:jiaoyebaobei080426@localhost:3306/db_name'
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    init_db()
    return "<hi>Hello World!</hi>"


@app.route('/shou')
def shouthesql():
    jg= Note.Query.all()
    return '<show>'+jg+'</show>'

def

app.run()
