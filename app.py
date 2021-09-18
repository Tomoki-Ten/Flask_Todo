from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from Models.Todo import Todo, TodoHandler, init_db

app = Flask(__name__)
db = init_db(app)
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

todo_handler = TodoHandler()

@app.route('/', methods=['GET'])
def index():
	todo_all = todo_handler.get_all()
	if not 'msg' in session:
	#if session['msg'] is None:
		session['msg'] = 'Normal1'
	
	return render_template('index.html',
							msg = session['msg'],
							todos = todo_all)

@app.route('/post', methods=['POST'])
def create():
	if request.method == 'POST':
		name = request.form['name']
		todo = request.form['todo']
		session['msg'] = None
		try:
			todo_handler.create(name, todo)
			session['msg'] = 'Create: Successfully Done.'
			return redirect(url_for('index', msg = session['msg']))
		except:
			session['msg'] = 'Create: Failed.'
			return redirect(url_for('index', msg = session['msg']))
	else:
		session['msg'] = 'Invalid Access'
		return redirect(url_for('index', msg=session['msg']))

@app.route('/update/<record_id>', methods = ['GET'])
@app.route('/update', methods=['POST'])
def update(record_id=None):
	session['msg'] = None
	if request.method == 'POST':
		todo_obj = todo_handler.find(request.form['id'])
		name = request.form['name']
		todo = request.form['todo']
		try:
			todo_handler.update(todo_obj, name, todo)
			session['msg'] = 'Update: Successfully Done.'
			return redirect(url_for('index', msg = session['msg']))
		except:
			session['msg'] = 'Update: Failed'
			return redirect(url_for('index', msg = session['msg']))
	else:
		record = todo_handler.find(record_id)
		if record is None:
			session['msg'] = 'No Record You Specified'
			return redirect(url_for('index', msg = session['msg']))

		return render_template('update.html', record = record)

@app.route('/delete/<record_id>', methods = ['GET'])
@app.route('/delete', methods = ['POST'])
def delete(record_id=None):
	session['msg'] = None
	if request.method == 'POST':
		record = todo_handler.find(request.form['id'])
		try:
			todo_handler.delete(record)
			session['msg'] = 'Delete: Successfully Done.'
			return redirect(url_for('index', msg = session['msg']))
		except:
			session['msg'] = 'Delete: Failed.'
			return redirect(url_for('index', status = msg))
	else:
		record = todo_handler.find(record_id)
		if record is None:
			session['msg'] = 'No Record You Specified.'
			return redirect(url_for('index', msg = session['msg']))

		return render_template('delete.html', record = record)
