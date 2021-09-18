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
		msg = 'Create: Successfully Done.'
		return redirect(url_for('index', status = msg))
		"""except:
			msg = 'Error'
			return redirect(url_for('index', status = msg))"""
	else:
		msg = 'Invalid Access'
		return redirect(url_for('index', status = msg))
#@app.route('/update', methods=['POST'])

@app.route('/delete/<record_id>', methods = ['GET'])
@app.route('/delete', methods = ['POST'])
def delete(record_id=None):
	if request.method == 'POST':
		record = todo_handler.find(request.form['id'])
		#try
		todo_handler.delete(record)
		#except
		msg = 'Delete: Successfully Done.'
		return redirect(url_for('index', status = msg))
	else:
		record = todo_handler.find(record_id)
		if record is None:
			msg = 'No Record You Specified.'
			return redirect(url_for('index', status = msg))

		return render_template('delete.html', record = record)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
