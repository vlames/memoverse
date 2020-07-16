# File: remverse.py
# Description: the file contains code to direct a user to an html page and remove a chosen verse from the database

from flask import redirect, url_for, render_template, request
from flask.views import MethodView
import model

class RemVerse(MethodView):
	def get(self):
		return render_template("remverse.html")
	
	def post(self):
		reference = request.form["book-name"].strip() + " " + request.form["book-chapter"].strip() + ":" + request.form["book-verse"].strip()
		appmodel = model.get_model()
		entries = [dict(reference=row[0], theme=row[1], verse=row[2], fums=row[3]) for row in appmodel.select()]
		for entry in entries:
			if reference.lower() == entry["reference"].lower():
				appmodel.remove(entry["reference"])
		return redirect(url_for('index'))