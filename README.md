Project features the following modifications from Assignment 2:

- any new forum posts that are submitted are immediately shown under "Recent posts"
- flashed message is shown when a post is submitted
- colour and style changes were added to forum posts for legibility and looks
- changed size and wording of webpage nagivation links
- "top of page" function added to page for convenience
- current date & time added to all pages
- added a DROP TABLE query that refreshes the posts database every time a user logs in

-----------------------------------------------------------------------------------------------------------
**Note: I wanted to upload a working webapp rather than upload one with many issues. However, 
I have pasted below some of my rough implementations that failed to work**

- attempt made to add a "Like" and "Dislike" button but could not get it fully functioning 
    -(removed... code that I had in models for like/dislike function shown below)

	
  models.py     {
	
	q = """
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    comment TEXT NOT NULL,
	likes INTEGER,
	dislikes INTEGER 
);
"""

def insertLike(like):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("UPDATE posts SET likes = likes + 1",(like))
    con.commit()
    con.close()


def retrieveLikes():
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT likes FROM posts")
    likes = cur.fetchall()
    con.close()
    return likes


def insertDislike(dislike):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("UPDATE posts SET dislikes = dislikes + 1",(dislike))
    con.commit()
    con.close()


def retrieveDislikes():
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT dislikes FROM posts")
    dislikes = cur.fetchall()
    con.close()
    return dislikes
}

And this was my implementation of like/dislike buttons in __init__.py

{
@app.route('/like', methods=['POST', 'GET'])
def like():
    if request.method == 'POST':
        like = request.form['l']
        models.insertLike(like)
        likes = models.retrieveLikes()
        posts = models.retrievePosts()
        return render_template('posts.html', likes=likes, posts=posts)
    else:
        likes = models.retrieveLikes()
        posts = models.retrievePosts()
        return render_template('posts.html', likes=likes, posts=posts)


@app.route('/dislike', methods=['POST', 'GET'])
def dislike():
    if request.method == 'POST':
        dislike = request.form['d']
        models.insertDislike(dislike)
        dislikes = models.retrieveDislikes()
        posts = models.retrievePosts()
        return render_template('posts.html', dislikes=dislikes, posts=posts)
    else:
        dislikes = models.retrieveDislikes()
        posts = models.retrievePosts()
        return render_template('posts.html', dislikes=dislikes, posts=posts)
}


---------------------------------------------------------------------------------------------------------

	
- attempt was also made to add a deletePost function but also had troubles with this (removed)  
   -(also removed ,wrote a deletePost function and tried to implement this in __init__.py but had issues)
   
-also created a "Create Account" page that uses a form to input a user/password and send the data
to a table called "users." However, I struggled to figure out what the python code would be in order
to check that the user/password input on /login = some user/password pair from data table.
Everything worked except I could not solve the missing code. Below were my implementations

Models.py

{
y = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
"""

def insertUser(user,password):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username,password) VALUES (?,?)",(user,password))
    con.commit()
    con.close()


def retrieveUsers():
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT username, password FROM users")
    users = cur.fetchall()
    con.close()
    return users
}



__init__.py    {

@app.route('/create', methods=['POST', 'GET'])
def createUser():
    if request.method == 'POST':
        if request.form['confirm'] != request.form['pass']:
            error = 'Passwords do not match. Please try again.'
        u = request.form['user']
        p = request.form['pass']
        models.insertUser(u,p)
        return render_template('createUser.html', error=error)
    else:
        return render_template('createUser.html')
}
	




