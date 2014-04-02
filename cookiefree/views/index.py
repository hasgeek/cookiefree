# -*- coding: utf-8 -*-

from flask import render_template, redirect, abort
from baseframe.views import gen_assets_url
from coaster.views import requestargs
from coaster.assets import AssetNotFound
from .. import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/asset')
@requestargs('asset[]')
def linkasset(asset):
    try:
        response = redirect(gen_assets_url(asset))
    except AssetNotFound:
        abort(404)
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response
