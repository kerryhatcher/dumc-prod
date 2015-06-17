__author__ = 'khatcher'


from flask import Flask, render_template, Markup
from flask_bootstrap import Bootstrap
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from smartencoding import smart_unicode
from flask.ext.mongoengine import MongoEngine

from pyBibleOrg import getVOTD

def register_blueprints(app):
    # Prevents circular imports
    from churchrunner.views import posts
    app.register_blueprint(posts, url_prefix='/posts')


app = Flask(__name__)
Bootstrap(app)
GoogleMaps(app)

# in a real app, these should be configured through Flask-Appconfig
app.config['SECRET_KEY'] = 'devkey'
app.config['RECAPTCHA_PUBLIC_KEY'] = \
    '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'

app.config["MONGODB_SETTINGS"] = {'DB': "my_tumble_log"}

#db = MongoEngine(app)

#register_blueprints(app)

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





