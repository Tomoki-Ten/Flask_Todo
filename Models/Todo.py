from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

def init_db(app):
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////app_data/todo.db'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	db.init_app(app)
	
class Todo(db.Model):
	__tablename__='todos'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(50))
	todo = db.Column(db.String(255))
	created_at = db.Column(db.DateTime, default=datetime.now)
	updated_at = db.Column(db.DateTime, default=datetime.now)

class TodoHandler:
	def create(self, name, todo):
		data = Todo(name = name, todo = todo)
		db.session.add(data)
		db.session.commit()

	def get_all(self):
		data = Todo.query.all()
		return data

	def find(self, id):
		data = Todo.query.filter_by(id = id).first()
		#data = Todo.query.get(id)
		return data
		
	def delete(self, todo):
		db.session.delete(todo)
		db.session.commit()
