import sqlite3 as sql

q = """
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    comment TEXT NOT NULL
);
"""



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