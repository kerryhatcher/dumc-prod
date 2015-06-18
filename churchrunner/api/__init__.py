__author__ = 'kwhatcher'

from flask.ext.cors import cross_origin
from flask import Blueprint, abort
from jinja2 import TemplateNotFound

from churchrunner.admin.helpers import requires_auth


api = Blueprint('api', __name__,
                        template_folder='templates'


                        )

@api.route('/')
@cross_origin(headers=['Content-Type', 'Authorization'])
@requires_auth
def show(page):
    try:
        return "All good. You only get this message if you're authenticated"
    except TemplateNotFound:
        abort(404)