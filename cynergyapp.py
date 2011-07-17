# -*- coding: utf-8 -*-
"""
    Cynergyapp
    ~~~~~~
    A basic crud app with simple controller actions.  This application was purpose built 
    as a demonstration of rapid development and core backend and UI concepts
"""

from __future__ import with_statement
from sqlite3 import dbapi2 as sqlite3
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
# Custom modules declarations
#from modules.database import db
# Model declarations
import database
from database import db_session

# create our little application :)
app = Flask(__name__)
app.config.from_pyfile('configuration.cfg')


@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run()
