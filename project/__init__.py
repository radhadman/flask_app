import models
from flask import Flask, Response, render_template, redirect, url_for, request, session, flash
from functools import wraps

app = Flask(__name__)

# config
app.secret_key = 'project'

# login decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
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
        flash('Your post was submitted!')
        name = request.form['x']
        comment = request.form['y']
        models.insertPost(name, comment)
        posts = models.retrievePosts()
        return render_template('posts.html', posts=posts)
    else:
        posts = models.retrievePosts()
        return render_template('posts.html', posts=posts)


@app.route('/deleterequest', methods=['POST', 'GET'])
def deleterequest():
        return render_template('delete.html')


@app.route('/deletepost', methods=['POST', 'GET'])
def deletepost():
    if request.method == 'POST':
        return render_template('delete.html')
		
@app.route('/deletesuccess', methods=['POST', 'GET'])
def deletesuccess():
    if request.method == 'POST':
        return render_template('deleteSuccess.html')


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)