from flask import Blueprint

contacts = Blueprint('contacts', __name__)

@contacts.route('/')
def home():
    return 'Contacts list' 

@contacts.route('/new')
def addcontact():
    return 'saving a contacts' 