from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from Models.Todo import Todo, TodoHandler, init_db

app = Flask(__name__)
db = init_db(app)

todo_handler = TodoHandler()

@app.route('/', methods=['GET'])
def index(status=None):
	todo_all = todo_handler.get_all()
	if status == None:
		msg = 'Normal'
	else:
		msg = status
		
	return render_template('index.html',
							msg = status,
							todos = todo_all)

@app.route('/post', methods=['POST'])
def create():
	if request.method == 'POST':
		name = request.form['name']
		todo = request.form['todo']
		#try:
		todo_handler.create(name, todo)
		msg = 'Successfully Done.'
		return redirect(url_for('index', status = msg))
		"""except:
			msg = 'Error'
			return redirect(url_for('index', status = msg))"""
	else:
		msg = 'Invalid Access'
		return redirect(url_for('index', status = msg))
#@app.route('/update', methods=['POST'])

#@app.route('/delete', methods=['POST'])
