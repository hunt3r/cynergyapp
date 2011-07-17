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
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# create our little application :)
app = Flask(__name__)
app.config.from_pyfile('config.cfg')
engine = create_engine('sqlite:////tmp/%s' % app.config["DATABASE"] , convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                      autoflush=False,
                                      bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

# Remove dbsessions at teardown
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

# Create the database if necessary
def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models
    Base.metadata.create_all(bind=engine)

"""
    Controller actions
"""

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/users/')
    def list_players():
    players = Player.query.all()
    app.logger.debug(&amp;quot;Player length %s &amp;quot;, len(players))
    a = &amp;quot;&amp;quot;
    d = {}
    for p in players:
    app.logger.debug(p.username)
    a = a + " " + p.username
    return "Hello Players: %s "  % (a)


if __name__ == '__main__':
    app.run()
