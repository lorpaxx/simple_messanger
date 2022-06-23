import os

import db_support
from flask import Flask, render_template, request

DB_FILE = r'data/db.sqlite'
MAX_LEN_MESSAGE = 1000
MAX_LEN_SENDER = 100

if not os.path.exists(DB_FILE):
    db_support.init_db(DB_FILE)

app = Flask(__name__)


@app.route('/')
def main_page():
    return 'Hello, welcome to Flask'


@app.route('/get_messages')
def get_messages():
    return {
        'messages': db_support.load_messages(DB_FILE)
    }


@app.route('/chat')
def display_chat():
    return render_template('form.html')


@app.route('/send_message')
def send_message():
    text = request.args['text']
    sender = request.args['name']
    if 0 < len(text) < MAX_LEN_MESSAGE and 0 < len(sender) < MAX_LEN_SENDER:
        db_support.add_message(DB_FILE, text, sender)
        return 'Ok'
    return 'Not Ok'


app.run(host='0.0.0.0', port=5000)
