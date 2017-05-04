#!/usr/bin/env python

from coaster.manage import init_manager
from cookiefree import app


if __name__ == '__main__':
    manager = init_manager(app, None)
    manager.run()
