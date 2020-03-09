from flask import request, jsonify, redirect, make_response
from mailutil import *

from models import *
from app import app

@app.route('/')
def index():
    return jsonify({
                'type': 'sucess',
                'data': 'It\'s working!'
            })

@app.route('/user/', methods = ['POST', 'GET'])
def user():
    token = request.args.get('email_token', default=False, type=str)
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
                    'data': 'not did possible to create user!!'
            }), 500
    else:
        return jsonify({
                'type': 'error',
                'data': 'token is expired!!'
        }), 500
    return jsonify({
            'type': 'sucess',
            'data': {
                'username': data['username'],
                'name': data['username'],
                'email': data['email']
            }
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
        return jsonify({
            'type': 'error',
            'data': 'user not found!!'
        }), 404

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
