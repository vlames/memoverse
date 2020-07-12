# File: index.py
# Description: the file contains code to direct a user to the main page

from flask import render_template
from flask.views import MethodView
class Index(MethodView):
	def get(self):
		return render_template("index.html")