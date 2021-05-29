from flask import Flask, render_template, request, session, redirect
from flask_session import Session
from random import choice
import database
from helpers import login_required
from tempfile import mkdtemp
app = Flask(__name__)

number_list = [
	100, 101, 200, 201, 202, 204, 206, 207, 300, 301, 302, 303, 304, 305, 307, 400, 401, 402, 403, 404, 405, 406, 408, 409, 410, 411, 412, 413, 414, 415,
	416, 417, 418, 421, 422, 423, 424, 425, 426,
	429, 431, 444, 450, 451, 500, 502, 503, 504, 506, 507, 508, 509, 510, 511, 599
]
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



@app.route('/')
def index():
	return render_template('index.html')

@app.route('/calendar')
# @login_required
def calendar():
  return render_template("calendar.html")


@app.route("/dailytasks", methods=["POST", "GET"])
# @login_required
def dailytasks():
  return render_template("dailytasks.html")

@app.route("/dailyemotions", methods=["POST", "GET"])
# @login_required
def dailyemotions():
  return render_template("dailyemotions.html")

@app.route("/login", methods=["POST", "GET"])
def login():
  session.clear()
  if request.method == "POST":
    if not request.form.get("username"):
      return render_template("error.html", error="You must enter a valid username")
    if not request.form.get("password"):
      return render_template("error.html", error="You must enter a valid password")
    username = request.form.get("username")
    password = request.form.get("password")
    if database.validLogin(username, password) == True:
      session["user_id"] = username
      print(session)
      return render_template("index.html")
    return render_template("error.html", error = "This is not a valid login")

  return render_template("login.html")


@app.route("/gethelp", methods=["POST", "GET"])
# @login_required
def gethelp():
  return render_template("gethelp.html")

@app.route("/create", methods=["POST", "GET"])
def create():
  if request.method == "POST":
    if not request.form.get("username"):
      return render_template("error.html", error = "You must enter a username")
    if not request.form.get("password"):
      return render_template("error.html", error = "You must enter a password")
    username = request.form.get("username")
    if database.existingUser(username) == True:
      return render_template("error.html", error = "This username is taken")
    password = request.form.get("password")
    password2 = request.form.get("password2")
    if password == password2:
      database.createUser(username, password)
      return render_template("login.html")
    return render_template("error.html", error="Passwords must match")
  return render_template("create.html")



@app.route('/user/', defaults={'username': None})
@app.route('/user/<username>')
def generate_user(username):
	if not username:
		username = request.args.get('username')

	if not username:
		return 'Sorry error something, malformed request.'

	return render_template('personal_user.html', user=username)

@app.route('/page')
def random_page():
  return render_template('page.html', code=choice(number_list))



if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug = True)