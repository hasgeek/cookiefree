#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from cookiefree import app

try:
    port = int(sys.argv[1])
except (IndexError, ValueError):
    port = 8020
app.run('0.0.0.0', port=port)
