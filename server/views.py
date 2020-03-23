from flask import request, jsonify, redirect, make_response
from app import app

from pages.models import *
from mailbox import *

import pages.user

@app.route('/')
def index():
    return jsonify({
                'type': 'sucess',
                'data': 'It\'s working!'
            })

# User section

@app.route('/user/', methods = ['POST'])
def user():
    return pages.user.user(request)

@app.route('/user/', methods = ['GET'])
def confirm_user_email():
    return pages.user.confirm_user_email(request)

@app.route('/user/<username>/')
def get_user(username):
    return pages.user.get_user(request, username)

# Event section

@app.route('/user/<username>/event/', methods=['POST', 'GET'])
def event(username):
    user = User.query.filter_by(username=username).first()
    if request.method == 'GET':
        if user:
            return jsonify({
                'type': 'sucess',
                'data': [ dict(
                    name=e.name,
                    description=e.description,
                    date=str(e.date),
                    fisic_ball=e.fisic_ball
                ) for e in Event.query.filter_by(owner=user).all()]
            })
        else:
            return jsonify({
                'type': 'error',
                'data': 'user not found!!'
            }), 404
    elif request.method == 'POST':
        print(request.cookies)
        log = request.cookies.get('bingonline.logged')
        log_user = request.cookies.get('bingonline.username')
        return 'ok!'
