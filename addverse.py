# File addverse.py
# Description: the file implements a class to direct a user to html page, submit data, and redirecting back to the main page

# Imports the necessary app modules
from flask import request, url_for, render_template
from flask.views import MethodView
import model
import json

# Defines the class to allow selection of data and insertion to database
class AddVerse(MethodView):
    # Directs a user to the html page for data selection
    def get(self):
        return render_template('addverse.html')
    # Directs the chosen data to the database and redirects user to the main page
    def post(self):
        """
        Accepts POST requests, and processes the chosen data;
        Redirect to index when completed.
        """
        req = request.get_json()
        req["redirect_url"] = url_for('index')
        appmodel = model.get_model()
        appmodel.insert(req["reference"], req["theme"], req["verse"], req["fums"])

        return json.dumps(req)
