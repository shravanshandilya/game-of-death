from app import app
from flask import render_template,send_from_directory,request
from random import randint
from character import character
characters = {};
GoT_Followers = 836664
char_file = open("char_data.txt","r")
for char in char_file:
	c = character(char,GoT_Followers)
	characters[char.split(",")[0].replace(" ","_")]=c

@app.route("/")
@app.route("/index")
def test():
	char = open("char_data.txt","r")
	chars=[]
	for line in char:
		chars.append(line.split(",")[0].replace(" ","_"))
	return render_template("index.html",chars=chars)

@app.route("/js/<path:path>")
def send_js(path):
	return send_from_directory("/static/js",path)

@app.route("/css/<path:path>")
def send_css(path):
	return send_from_directory("/static/css",path)


@app.route("/how-it-works")
def send_how():
	return render_template("how-it-works.html")


@app.route("/char")
def send_char():
	print characters.keys()," ",request.args['name']
	if "name" in request.args and characters:
		c = characters[str(request.args['name'])]
		print c
		if c != None:
			return render_template("char.html",char=c.get_formatted_name(),test = [c.get_probabality(),c.get_popularity(),c.get_good_or_bad(),c.get_importance(),c.get_age()])
		else:
			return "working"
	else:
		return "problem"

@app.route("/pb_test")
def pb_test():
	test = []
	test.append(randint(0,100))
	test.append(randint(0,100))
	test.append(randint(0,100))
	test.append(randint(0,100))
	return render_template("pb_test.html",test = test)
	
