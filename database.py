import sqlite3
from sqlite3 import IntegrityError

con = sqlite3.connect("users.db")

cur = con.cursor()

def createUser(username, password):
  try: 
    cur.execute("""
      insert into Users (username, password) values (?, ?)
    """, (username, password))
    return True
  except IntegrityError:
    return False