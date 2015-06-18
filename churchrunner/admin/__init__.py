__author__ = 'kwhatcher'

import os
import json

from flask import Blueprint, abort
from jinja2 import TemplateNotFound
import requests
from flask import request, session, redirect

from models import *
from churchrunner.admin.helpers import requires_auth


admin_pages = Blueprint('admin_pages', __name__,
                        template_folder='templates'


                        )







@admin_pages.route('/')
@requires_auth
def index():


    return "All good. You only get this message if you're authenticated"


# Here we're using the /callback route.
@admin_pages.route('/callback')
def callback_handling():
  env = os.environ
  code = request.args.get('code')

  json_header = {'content-type': 'application/json'}

  token_url = "https://{domain}/oauth/token".format(domain=os.environ.get('AUTH0_DOMAIN'))

  token_payload = {
    'client_id':     os.environ.get('AUTH0_CLIENT_ID'),
    'client_secret': os.environ.get('AUTH0_CLIENT_SECRET'),
    'redirect_uri':  request.url_root + 'admin/callback',
    'code':          code,
    'grant_type':    'authorization_code'
  }

  token_info = requests.post(token_url, data=json.dumps(token_payload), headers = json_header).json()

  user_url = "https://{domain}/userinfo?access_token={access_token}" \
      .format(domain=os.environ.get('AUTH0_DOMAIN'), access_token=token_info['access_token'])

  user_info = requests.get(user_url).json()

  # We're saving all user information into the session
  session['profile'] = user_info

  # Redirect to the User logged in page that you want here
  # In our case it's /dashboard
  return redirect('/admin')