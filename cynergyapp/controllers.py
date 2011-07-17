from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask import jsonify
from cynergyapp import app
from cynergyapp.database import db_session
from cynergyapp.models import Entry

"""
    Controller Helper methods
"""
#get a list of known types
# Todo use lookup table for get these data
def getTypes():
    return ['Type 1', 'Type 2', 'Type 3']



"""
    JSON Controllers
"""
@app.route('/_get_types', methods=['GET'])
def get_types_as_JSON():
    return jsonify(types = getTypes())


@app.route('/_get_entries', methods=['GET'])
def update_entry():
    for entry in Entry.query.all()
        print entry
    return '{"test1", "test2"}'



"""
    HTML Controller actions are defined below.
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
# use a schema to generate this objects params
@app.route('/add', methods=['POST'])
def add_entry():
    #e = new Entry()
    entry = Entry(request.form['name'], 
                  request.form['type'],
                  request.form['library'],
                  request.form['from_buss'],
                  request.form['to_buss'],
                  request.form['length'],
                  request.form['ampacity'])
    db_session.add(entry)
    db_session.commit()
    return redirect(url_for('home'))
    
# Get the add form
@app.route('/add', methods=['GET'])
def entry_add_form():
    return render_template('entry_form.html', 
                            title='Add', 
                            types=getTypes())


# Get the edit form
# TODO: get the entry by ID
@app.route('/edit', methods=['GET'])
def entry_edit_form():
    entry = Entry.query.all()
    return render_template('entry_form.html', 
                            title='Edit', types=getTypes(),
                            entry=entry)


