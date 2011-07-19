# Cynergyapp

A basic crud app with simple controller actions.  This application was purpose built 
as a demonstration of rapid development and core backend and UI concepts

## Requires
* simplejson
* Flask-SqlAlchemy 
* http://pypi.python.org/pypi/Flask-SQLAlchemy

## Setup
edit config.cfg and change your database path to match your environment

### Initialize your database
* cd to project
* python 
* from cynergyapp.database import init_db
* init_db()
* exit python
* then from bash: python run.py