#!/usr/bin/env python

from coaster.manage import init_manager
from cookiefree import app, init_for


if __name__ == '__main__':
    manager = init_manager(app, None, init_for)
    manager.run()
