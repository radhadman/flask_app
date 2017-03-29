from flask import Flask, Response, render_template, redirect, url_for, request, session, flash, g
from functools import wraps
import sqlite3

app = Flask(__name__)

# config
app.secret_key = 'assign2key'
app.database = 'database.db'

# login decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Please login.')
            return redirect(url_for('login'))
    return wrap
	
@app.route('/posts')
@login_required
def blog():
    g.db = connect_db()
    cur = g.db.execute('select * from posts')
    posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
    g.db.close()
    return render_template('posts.html', posts=posts)  # render a template
	
	
@app.route('/')
@login_required
def home():
	return render_template('index.html')	
	

@app.route('/out')
def out():
    return render_template('logout.html')

	
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid username/password. Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

	
@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You have been logged out.')
    return redirect(url_for('out'))
	
	
@app.route('/posts', methods=['POST', 'GET'])
def posts():
	return render_template('posts.html')
	

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
	
	

        
