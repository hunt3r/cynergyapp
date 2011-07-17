# -*- coding: utf-8 -*-
"""
    Cynergyapp
    ~~~~~~
    A basic crud app with simple controller actions.  This application was purpose built 
    as a demonstration of rapid development and core backend and UI concepts
"""

from __future__ import with_statement
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# create our little application :)
app = Flask(__name__)
app.config.from_pyfile('config.cfg')

import cynergyapp.database
import cynergyapp.controllers



if __name__ == '__main__':
    app.run()
