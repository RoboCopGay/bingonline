from flask import request, jsonify, redirect, abort

from models import *
from app import app

@app.route('/user', methods = ['POST'])
def user():
    if request.method == 'POST':
        create_user(
            name = request.json['name'].strip(),
            username = request.json['username'].strip(),
            email = request.json['email'].strip(),
            password = bytes(request.json['password'].strip(), 'utf-8'),
            address = reguest.json['address']
        )
        return jsonify(request.json)

@app.route('/user/<username>')
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
