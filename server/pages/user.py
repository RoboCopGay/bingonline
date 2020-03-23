from flask import request, jsonify, redirect, make_response

from database.models import *
from mailbox import *

def user():
    data = request.json['data']
    if request.json['type'] == 'create':
        email = data['email'].strip()

        if not User.query.filter_by(email=email).first():
            if check_email_validation(email):
                send_confirmation_mail(request.json['data'])
            else:
                return jsonify({
                    'type': 'error',
                    'data': 'email is not valid!'
                }), 500
        else:
            return jsonify({
                'type':  'error',
                'data':  'user did exists!'
            })
        return jsonify({
            'type':  'sucess',
            'data':  data
        })

    elif request.json['type'] == 'login':
        response = make_response(jsonify({
            'type': 'sucess',
            'data': 'login realized!'
        }))

        if request.cookies.get('bingonline.logged'):
            return response

        if 'password' in data:

            user = None
            if 'username' in data:
                user = User.query.filter_by(username=data['username']).first()
            elif 'email' in data:
                user = User.query.filter_by(email=data['email']).first()
            else:
                return jsonify({
                    'type': 'error',
                    'data': 'No user credentials (username or email) on request'
                }), 500

            if user:
                if user.check_pass(data['password']):
                    return response

            else:
                return jsonify({
                    'type': 'error',
                    'data': 'user not found!!'
                }), 404
        else:
            return jsonify({
                'type': 'error',
                'data': 'No user credentials (password) on request'
            }), 500

def confirm_user_email():
    token = request.args.get('email_token', default=False, type=str)

    if token:
        data = confirm_token(token)
        if data:
            try:
                user = create_user(
                    username = data['username'],
                    name = data['name'],
                    email = data['email'],
                    password = data['password'],
                    address = data['address']
                )

                if user and User.query.filter_by(email=data['email'], username=data['username']).first():
                    db.session.add(user)
                    db.session.commit()
            except:
                return jsonify({
                        'type': 'error',
                        'data': 'not did possible to create user!'
                }), 500
        else:
            return jsonify({
                    'type': 'error',
                    'data': 'token is expired or do not exists!'
            }), 500
    return jsonify({
            'type': 'sucess',
            'data': {
                'username': data['username'],
                'name': data['username'],
                'email': data['email']
            }
    })

def get_user(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify(dict(
            name = user.name,
            username = user.username,
            email = user.email
        ))
    else:
        return jsonify({
            'type': 'error',
            'data': 'user not found!!'
        }), 404
