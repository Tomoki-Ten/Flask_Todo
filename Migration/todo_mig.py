from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////app_data/todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
	__tablename__ = 'todos'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(50))
	todo = db.Column(db.String(255))
	created_at = db.Column(db.DateTime, default=datetime.now)
	updated_at = db.Column(db.DateTime, default=datetime.now)

# [*] Execute these commands on your terminal
# sudo python3
# from Migration.todo_mig import db
# db.create_all()
