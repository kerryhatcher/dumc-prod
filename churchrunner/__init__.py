from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from smartencoding import smart_unicode
from flask.ext.mongoengine import MongoEngine
from flask.ext.heroku import Heroku
import os
from raygun4py import raygunprovider
from raygun4py.middleware import flask
import sys

from pyBibleOrg import getVOTD


def register_blueprints(app):
    # Prevents circular imports
    #from churchrunner.views import posts
    from churchrunner.admin import admin_pages
    #app.register_blueprint(posts, url_prefix='/posts')
    app.register_blueprint(admin_pages, url_prefix='/admin')


app = Flask(__name__)
Bootstrap(app)
GoogleMaps(app)
heroku = Heroku(app)
flask.Provider(app, os.environ.get('RAYGUN_APIKEY')).attach()
# in a real app, these should be configured through Flask-Appconfig
app.config['SECRET_KEY'] = os.environ.get('FLASK-KEY')


app.config['MONGODB_USERNAME'] = app.config['MONGODB_USER']

db = MongoEngine(app)

register_blueprints(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=32.7655043,
        lng=-83.8485504,
        markers=[(32.7655043, -83.8485504)],
        zoom=15,
        style="height:400px;width:700px;"
        )
    return render_template('about.html', mymap=mymap)


@app.context_processor
def inject_VOTD():
    votd=smart_unicode(getVOTD())
    return dict(votd=votd)

@app.context_processor
def inject_login_callback():
    callbackURL = request.url_root + 'admin/callback'
    return dict(callbackURL=callbackURL)


def handle_exception(exc_type, exc_value, exc_traceback):
    sender = raygunprovider.RaygunSender(os.environ.get('RAYGUN_APIKEY'))
    sender.send_exception(exc_info=(exc_type, exc_value, exc_traceback))

sys.excepthook = handle_exception