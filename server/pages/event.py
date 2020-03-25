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
            return jsonify({'user': str(session.get('user'))})
        else:
            return jsonify({
                'type': 'error',
                'data': 'You need to be logged to acess this page!'
            }), 403
