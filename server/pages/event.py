from flask import request, jsonify, redirect, make_response
from database.models import *

from .user import session

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
        if session.get('user'):
            data = request.json['data']
            if request.json['type'] == 'create':

                owner = User.query.filter_by(username=session.get('user').username).first()
                print(f'\n\n\n\n{"-"*5}{owner}{"-"*5}\n\n\n')

                event = create_event(
                    name = data['name'],
                    description = data['description'],
                    date = data['date'],
                    fisic_ball = data['fisic_ball'],
                    owner = owner
                )
                return jsonify({
                    'type': 'sucess',
                    'data': dict(
                        name=event.name,
                        description=event.description,
                        date=str(event.date),
                        fisic_ball=event.fisic_ball
                    )
                })
        else:
            return jsonify({
                'type': 'error',
                'data': 'You need to be logged to acess this page!'
            }), 403
