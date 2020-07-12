# File: viewverses.py
# Description: defines the class and method to allow user to view stored verses

# Imports the necessary app modules
from flask import render_template
from flask.views import MethodView
import model

class ViewVerses(MethodView):
	def get(self):
		return render_template("viewverses.html")