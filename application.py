"""
A simple app for The Bible verse memorization
"""
import flask
from flask.views import MethodView
from index import Index
from viewverses import ViewVerses
from addverse import AddVerse
from process import Process
from display import Display

# Instantiates the flask app object
application = flask.Flask(__name__)

# Specifies the page to serve for the route "/"
application.add_url_rule('/', view_func=Index.as_view('index'), methods=["GET"])
# Specifies the page to serve for the route "viewverse"
application.add_url_rule('/viewverse/', view_func=ViewVerses.as_view('viewverses'), methods=["GET"])
# Specifies the page to serve and submit information through for the route "addverse"
application.add_url_rule('/addverse/', view_func=AddVerse.as_view('addverse'), methods=['GET', 'POST'])
# Specifies the resource to serve and return information through for the route "process"
application.add_url_rule('/process/', view_func=Process.as_view('process'), methods=['POST'])
# Specifies the resource to serve and return information through for the route "display"
application.add_url_rule('/display/', view_func=Display.as_view('display'), methods=['POST'])

# Runs the application on port 8000 with debugging enabled
if __name__ == '__main__':
    application.run(debug=True)