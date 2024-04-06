from flask import Blueprint, render_template

contacts = Blueprint('contacts', __name__)

@contacts.route('/')
def home():
    return render_template('index.html')

@contacts.route('/new')
def addcontact():
    return 'saving a contacts' 