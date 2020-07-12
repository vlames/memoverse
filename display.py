# File: display.py
# Description: the file contains code that supplies the javascript file with memoverse data from a database

from flask.views import MethodView, request
import model
import json


class Display(MethodView):
    def post(self):
        appmodel = model.get_model()
        entries = [dict(reference=row[0], theme=row[1], verse=row[2], fums=row[3]) for row in appmodel.select()]
        return json.dumps(entries)