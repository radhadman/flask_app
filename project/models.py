import sqlite3 as sql


x = """
DROP TABLE IF EXISTS posts;
"""


q = """
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    comment TEXT NOT NULL,
	likes SMALLINT,
	dislikes SMALLINT
);
"""

con = sql.connect("database.db")
cur = con.cursor()
cur.execute(x)


con = sql.connect("database.db")
cur = con.cursor()
cur.execute(q)


def insertPost(name,comment):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO posts (name,comment) VALUES (?,?)",(name,comment))
    con.commit()
    con.close()


def retrievePosts():
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT name, comment FROM posts")
    posts = cur.fetchall()
    con.close()
    return posts
	
	
def insertLike(like):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("UPDATE posts SET likes = likes + 1",(like)
    con.commit()
    con.close()


def retrieveLikes():
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT count(likes) FROM posts")
    likes = cur.fetchall("SELECT likes FROM posts")
    con.close()
    return likes


def insertDislike(dislike):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("UPDATE posts SET dislikes = dislikes + 1",(dislike)
    con.commit()
    con.close()


def retrieveDislikes():
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT count(dislikes) FROM posts")
    dislikes = cur.fetchall("SELECT dislikes FROM posts")
    con.close()
    return dislikes