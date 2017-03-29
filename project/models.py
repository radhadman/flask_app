import sqlite3 as sql

q = """
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    blogpost TEXT NOT NULL    
);
"""

con = sql.connect("database.db")
cur = con.cursor()
cur.execute(q)

def insertPost(blogpost):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO posts (blogpost) VALUES (?)",(blogpost))
    con.commit()
    con.close()

def retrievePosts():
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT blogpost FROM posts")
    users = cur.fetchall()
    con.close()
    return posts
