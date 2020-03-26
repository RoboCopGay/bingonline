from flask import request, jsonify, redirect, make_response

from database.models import *
from mailbox import *

from session import session

def user():
    if request.method == 'POST':
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

            if session.get('user'):
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

                session['user'] = user
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
        elif request.json['type'] == 'logout':
            user_logged = session.get('user').username if session.get('user') else None
            if user_logged:
                session.pop('user', None)
                return jsonify({
                    'type': 'sucess',
                    'data': f'User {user_logged} are disconnected!'
                })
            else:
                return jsonify({
                    'type': 'error',
                    'data': 'No logged user!'
                }), 500
    return jsonify({
        'type': 'error',
        'data': 'Invalid request!'
    }), 400

def confirm_user_email(token):
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
                    'name': data['name'],
                    'email': data['email']
                }
        })
    else:
        return jsonify({
            'type': 'error',
            'data': 'Invalid request!'
        }), 400

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
