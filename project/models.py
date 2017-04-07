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
    posts = cur.fetchall()
    con.close()
    return posts
	

def retrievePosts():
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT name, comment FROM posts")
    posts = cur.fetchall()
    con.close()
    return posts
	
	
def deletePost(id):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("DELETE FROM posts (name,comment) WHERE id=?",(id))
    con.commit()
    con.close()
	
	