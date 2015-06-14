__author__ = 'khatcher'


from flask import Flask, render_template
from flask_bootstrap import Bootstrap



app = Flask(__name__)
Bootstrap(app)

# in a real app, these should be configured through Flask-Appconfig
app.config['SECRET_KEY'] = 'devkey'
app.config['RECAPTCHA_PUBLIC_KEY'] = \
    '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'


@app.route('/')
def home():
    return render_template('index.html')







