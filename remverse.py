# File: remverse.py
# Description: the file contains code to direct a user to an html page and remove a chosen verse from the database

from flask import redirect, url_for, render_template
from flask.views import MethodView
class RemVerse(MethodView):
	def get(self):
		return render_template("remverse.html")
	
	def post(self):
		return redirect(url_for('index'))