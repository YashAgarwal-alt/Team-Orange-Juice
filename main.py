from flask import Flask, render_template, request
from random import choice

app = Flask(__name__)

number_list = [
	100, 101, 200, 201, 202, 204, 206, 207, 300, 301, 302, 303, 304, 305, 307, 400, 401, 402, 403, 404, 405, 406, 408, 409, 410, 411, 412, 413, 414, 415,
	416, 417, 418, 421, 422, 423, 424, 425, 426,
	429, 431, 444, 450, 451, 500, 502, 503, 504, 506, 507, 508, 509, 510, 511, 599
]

@app.route('/')
def index():
	return render_template('index.html')

# W userlogin done already

@app.route('/calendar')
def calendar():
  return render_template("calendar.html")


@app.route("/dailytasks", methods=["POST", "GET"])
def dailytasks():
  return render_template("dailytasks.html")

@app.route("/dailyemotions")
def dailyemotions(methods=["POST"]):
  return render_template("dailyemotions.html")

@app.route("/login", methods=["POST", "GET"])
def login():
  if request.method == "POST":
    if not request.form.get("username"):
      return render_template("error.html", error="You must enter a valid username")
    if not request.form.get("password"):
      return render_template("error.html", error="You must enter a valid password")
    username = request.form.get("username")
    print(username)
    return render_template("index.html")


  return render_template("login.html")


@app.route("/gethelp", methods=["POST", "GET"])
def gethelp():
  return render_template("gethelp.html")

@app.route("/create")
def create(methods=["POST", "GET"]):
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