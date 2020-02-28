from flask import request, jsonify, redirect, abort
from mailutil import *

from models import *
from app import app

@app.route('/')
def index():
    return jsonify({
                'type':'sucess',
                'data':'It\'s working!'
            })

@app.route('/user/', methods = ['POST'])
def user():
    email = request.json['email'].strip()
    if check_email_validation(email):
        send_confirmation_mail(request.json)
    else:
        return jsonify({
            'type':'error',
            'data':'email is not valid!'
        })
    return jsonify({
        'type': 'sucess',
        'data': request.json
    })

@app.route('/user/confirm_email/<token>/')
def confirm_email(token):
    data = confirm_token(token)
    if data:
        user = create_user(
            username = data['username'],
            name = data['name'],
            email = data['email'],
            password = data['password'],
            address = data['address']
        )
        if user:
            db.session.add(user)
            db.session.commit()
        else:
            return jsonify({
                    'type':'error',
                    'data':'USER is FUCKED!!'
            })
    else:
        return jsonify({
                'type':'error',
                'data':'DATA is FUCKED!!'
        })
    return jsonify({
            'type':'sucess',
            'data':'It\'s working!'
    })

@app.route('/user/<username>/')
def get_user(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify(dict(
            name = user.name,
            username = user.username,
            email = user.email
        ))
    else:
        abort(404)
