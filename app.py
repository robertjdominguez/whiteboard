from twilio import twiml
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import time
import random

'''
Basic Flask app utilizing Twilio to update a board whenever I text it.
I plan on utiliting it for letting people know where I am at school, and telling
my students which materials they'll need for class that day.

Process:
(1) Enable Twilio client to receive texts via endpoint
(2) On receipt of text with conditional message, update db
(3) Have AJAX calls running on the index page to update the text from the db
'''

app = Flask(__name__)


# DB Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
db = SQLAlchemy(app)

# Update table
class Updates(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    msg = db.Column(db.String)
    materials = db.Column(db.String)

#Route handling
@app.route('/')
def index():
    update = Updates.query.filter_by(id=1).first()

    return render_template('index.html', update=update)

@app.route('/update', methods=['POST'])
def update_text():
    number = request.form['From']
    message_body = request.form['Body']
    global message_body_string
    message_body_string = str(message_body)

    resp_update = twiml.Response()

    if "Update" in message_body:
       resp_update.message('Updating the board now')
       # Split the message after the colon (this is what we want to use for upd.)
       update = message_body.split(":",1)[1]
       print(update)

       # Pass the update into the db where id = 1
       updated_msg = Updates.query.filter_by(id=1).first()
       updated_msg.msg = update
       db.session.commit()

       return str(resp_update)

    if "Materials" in message_body:
       resp_update.message('Updating the board for students now')
       # Split the message after the colon (this is what we want to use for upd.)
       material_update = message_body.split(":",1)[1]
       print(material_update)

       # Pass the update into the db where id = 1
       updated_materials = Updates.query.filter_by(id=1).first()
       updated_materials.materials = material_update
       db.session.commit()

       return str(resp_update)

if __name__ == "__main__":
    app.run()
