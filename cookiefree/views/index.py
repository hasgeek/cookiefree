# -*- coding: utf-8 -*-

from flask import render_template, abort, redirect
from flask.ext.assets import Bundle
from baseframe import assets
from coaster.utils import make_name
from coaster.assets import split_namespec
from coaster.views import requestargs
from .. import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/asset')
@requestargs('asset[]')
def linkasset(asset):
    try:
        names = [split_namespec(a)[0] for a in asset]
    except ValueError:
        abort(400)

    is_js = reduce(lambda status, name: status and name.endswith('.js'), names, True)
    is_css = reduce(lambda status, name: status and name.endswith('.css'), names, True)
    output_name = make_name('-'.join(asset).replace(
        '==', '-eq-').replace('>', '-gt-').replace('<', '-lt-').replace('>=', '-gte-').replace('<=', '-lte-'))
    if is_js:
        bundle = Bundle(assets.require(*asset), output='gen/' + output_name + '.js', filters='closure_js')
    elif is_css:
        bundle = Bundle(assets.require(*asset), output='gen/' + output_name + '.css', filters=['cssrewrite', 'cssmin'])
    else:
        abort(400)

    response = redirect(bundle.urls(env=app.assets)[0])
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response
