from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('table')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:yeningyuan@localhost/db_name'
db = SQLAlchemy(app)


class Note(db.Model):
    id = db.Column(db.INTEGER, nullable=False, )
    body = db.Column(db.TEXT, nullable=False)


def init_db():
    db.create_all()


uesrs = {

    'admin': ['admin', 'look', 'delete', 'add']

}
