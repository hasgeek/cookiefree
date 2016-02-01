# -*- coding: utf-8 -*-

from flask import render_template, redirect
from baseframe.views import gen_assets_url
from coaster.views import requestargs
from coaster.assets import AssetNotFound
from .. import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/asset')
@requestargs('asset[]', 'a[]')
def linkasset(asset=[], a=[]):
    assets = asset + a  # `asset` and `a` are both lists; merge them
    try:
        response = redirect(gen_assets_url(assets))
    except AssetNotFound as e:
        return "404 Not found: %s" % unicode(e), 404
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.after_request
def allow_cross_origin(response):
    # In production, assets are directly served by Nginx or Apache,
    # so make sure the same header is set in the web server's config
    response.headers.setdefault('Access-Control-Allow-Origin', '*')
    return response
