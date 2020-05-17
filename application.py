import datetime
from flask import Flask, render_template

app=Flask(__name__)


@app.route("/")
def index():
	today=datetime.datetime.now()
	if today.date==1 and today.month==1:
		new_year=True
	else:
		new_year=False


	return render_template("index.html",var=new_year)
