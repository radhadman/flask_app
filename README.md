Project features the following modifications from Assignment 2:

- any new forum posts that are submitted are immediately shown under "Recent posts"
- flashed message is shown when a post is submitted
- colour and style changes were added to forum posts for legibility and looks
- changed size and wording of webpage nagivation links
- "top of page" function added to page for convenience
- current date & time added to all pages
- added a DROP TABLE query that refreshes the posts database every time a user logs in

-----------------------------------------------------------------------------------------------------------

- attempt made to add a "Like" and "Dislike" button but could not get it fully functioning 
    -(removed... code that I had in models for like/dislike function shown below)
{

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

Table for posts was this: 

q = """
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    comment TEXT NOT NULL,
	likes INTEGER,
	dislikes INTEGER 
);
"""
	
- attempt was also made to add a deletePost function but also had troubles with this (removed)  
   -(also removed ,wrote a deletePost function and tried to implement this in __init__.py but had issues)
	
**Note: I wanted to upload a working webapp rather than upload one with many issues.**



