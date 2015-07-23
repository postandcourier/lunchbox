#!/usr/bin/env python
"""
Example application views.

Note that `render_template` is wrapped with `make_response` in all application
routes. While not necessary for most Flask apps, it is required in the
App Template for static publishing.
"""

import app_config
import json
import oauth
import static

from flask import Flask, make_response, render_template
from render_utils import make_context, smarty_filter, urlencode_filter
from werkzeug.debug import DebuggedApplication

app = Flask(__name__)
app.debug = app_config.DEBUG

app.add_template_filter(smarty_filter, name='smarty')
app.add_template_filter(urlencode_filter, name='urlencode')

@app.route('/')
@app.route('/index.html')
@oauth.oauth_required
def index():
    """
    Example view demonstrating rendering a simple HTML page.
    """
    context = make_context()
    context['name'] = 'Home'
    return make_response(render_template('index.html', **context))

@app.route('/factlist/index.html')
@oauth.oauth_required
def factlist():
    context = make_context()
    context['name'] = 'Factlist'
    return make_response(render_template('factlist.html', **context))

@app.route('/quotable/index.html')
@oauth.oauth_required
def quotable():
    context = make_context()
    context['name'] = 'Quotable'
    return make_response(render_template('quotable.html', **context))

@app.route('/waterbug/index.html')
@oauth.oauth_required
def waterbug():
    context = make_context()
    context['name'] = 'Waterbug'
    return make_response(render_template('waterbug.html', **context))

app.register_blueprint(static.static)
app.register_blueprint(oauth.oauth)

# Enable Werkzeug debug pages
if app_config.DEBUG:
    wsgi_app = DebuggedApplication(app, evalex=False)
else:
    wsgi_app = app

# Catch attempts to run the app directly
if __name__ == '__main__':
    print 'This command has been removed! Please run "fab app" instead!'
