from flask import Flask, Response, render_template, redirect, url_for, request, session, flash
from functools import wraps
import models

app = Flask(__name__)

# config
app.secret_key = 'assign2key'

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
    if request.method == 'POST':
        name = request.form['name']
        comment = request.form['comment']
        models.insertPost(name, comment)
        return render_template('posts.html')
    else:
        p = models.retrievePosts()
        return render_template('posts.html', p=p)
	

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
	

        
