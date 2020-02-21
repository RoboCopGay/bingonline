from flask import render_template, request, jsonify

from models import *
from app import app

@app.route('/user/add', methods = ['POST', 'GET'])
def add_user():
    if request.method == 'POST':
        create_user(
            name = request.json['name'].strip(),
            username = request.json['username'].strip(),
            email = request.json['email'].strip(),
            password = bytes(request.json['password'].strip(), 'utf-8'),
            address = create_address(
                cep = request.json['address']['cep'],
                city = request.json['address']['city'],
                state = request.json['address']['state'],
                number = request.json['address']['number'],
                street = request.json['address']['street'],
                country = request.json['address']['country'],
                neighborhood = request.json['address']['neighborhood']
            )
        )
        return jsonify(request.json)
    elif request.method == 'GET':
        return '...'
