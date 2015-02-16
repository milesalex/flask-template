import os
from flask import Flask, render_template
from flask.ext.assets import Environment, Bundle
from flaskext.markdown import Markdown
import requests
from datetime import datetime

app = Flask(__name__, static_url_path='')
assets = Environment(app)
Markdown(app)

scss = Bundle('styles/scss/reset.scss', 'styles/scss/styles.scss', filters='pyscss', output='styles/css/all.css')
assets.register('scss_all', scss)

js = Bundle('javascript/jquery.js','javascript/scripts.js', filters='jsmin', output='javascript/all.js')
assets.register('js_all', js)

@app.route('/')
def index():
  return render_template('index.html')

from werkzeug import SharedDataMiddleware
if __name__ == '__main__':
  if app.debug:
    app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
      '/static': static_folder
    })
  app.run(debug = True, use_debugger = True, use_reloader = True)
