from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from cynergyapp import app
from cynergyapp.database import db_session
from cynergyapp.models import Entry

"""
    Controller actions are defined below.
"""


# Entries list
@app.route('/')
def home():
    entries = Entry.query.all()
    return render_template('show_entries.html', 
                            entries=entries)


# TODO: will need to check session here 
# Add a login
# Add entries w/this route
@app.route('/add', methods=['POST'])
def add_entry():
    #e = new Entry()
    return redirect(url_for('home'))
    
# Get the add form
@app.route('/add', methods=['GET'])
def entry_add_form():
    return render_template('entry_form.html')


# Get the edit form
# TODO: get the entry by ID
@app.route('/edit', methods=['GET'])
def entry_edit_form():
    entry = Entry.query.all()
    return render_template('entry_form.html', 
                            entry=entry)


