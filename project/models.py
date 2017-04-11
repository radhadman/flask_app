import sqlite3 as sql


x = """
DROP TABLE IF EXISTS posts;
"""


q = """
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    comment TEXT NOT NULL
);
"""


y = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
"""

con = sql.connect("database.db")
cur = con.cursor()
cur.execute(y)


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


def insertUser(user,password):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username,password) VALUES (?,?)",(user,password))
    con.commit()
    con.close()