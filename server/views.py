from flask import request, jsonify, redirect, make_response

from pages.user import session
from app import app

from database.models import *
from mailbox import *

import pages.user, pages.event

# Index
@app.route('/')
def index():
    return jsonify({
                'type': 'sucess',
                'data': 'It\'s working!'
            })



# User section
@app.route('/user/', methods = ['POST', 'GET'])
def user():
    if request.method == 'POST':
        return pages.user.user()
    else:
        token = request.args.get('email_token', default=False, type=str)
        if token:
            return pages.user.confirm_user_email(token)
        else:
            return pages.user.user()

@app.route('/user/<username>/')
def get_user(username):
    return pages.user.get_user(username)



# Event section
@app.route('/event/<username>/', methods=['POST', 'GET'])
def event(username):
    user = User.query.filter_by(username=username).first()
    if user:
        if request.json and request.json['type'] == 'add_prize':
            event_id = request.args.get('event_id', default=False, type=int)
            event = Event.query.filter_by(id=event_id).first() if event_id else None
            if event:
                return pages.event.prize(user, event)
            else:
                return jsonify({
                    'type': 'error',
                    'data': 'event not found!!'
                }), 404
        else:
            return pages.event.event(user)
    else:
        return jsonify({
            'type': 'error',
            'data': 'user not found!!'
        }), 404
