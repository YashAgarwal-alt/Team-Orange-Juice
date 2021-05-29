import sqlite3
from sqlite3 import IntegrityError



def createUser(username, password):
  con = sqlite3.connect("users.db")
  cur = con.cursor()  
  try: 
    cur.execute("""
      insert into Users (Username, Password) values (?, ?)
    """, (username, password))
    con.commit()
    con.close()
    return True
  except IntegrityError:
    return False


def existingUser(username):
  con = sqlite3.connect("users.db")
  cur = con.cursor()

  username = cur.execute("""
    select * from Users where Username = ?
  """, (username, )).fetchone()
  if username == None:
    return False
  return True


def validLogin(username, password):
  con = sqlite3.connect("users.db")
  cur = con.cursor()

  valid = cur.execute("""
    select * from Users where Username = ? and Password = ?
  """, (username, password)).fetchone()
  if valid == None:
    return False
  return True