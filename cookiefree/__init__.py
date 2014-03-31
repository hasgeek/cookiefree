# -*- coding: utf-8 -*-

# The imports in this file are order-sensitive

from __future__ import absolute_import
from flask import Flask
from baseframe import baseframe, assets, Version
import coaster.app
from ._version import __version__

version = Version(__version__)

# First, make an app

app = Flask(__name__, instance_relative_config=True)

# Second, import the models and views

from . import views

# Third, setup baseframe and assets

assets['cookiefree.js'][version] = 'js/app.js'
assets['cookiefree.css'][version] = 'css/app.css'


# Configure the app
def init_for(env):
    coaster.app.init_app(app, env)
    baseframe.init_app(app, requires=['baseframe-bs3', 'cookiefree'])
