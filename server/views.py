from flask import render_template, request

from models import User, create_user
from app import app


@app.route('/')
def index():

    users = User.query.all()

    return render_template('index.html', users=users)


@app.route('/add', methods=['GET', 'POST'])
def add():

    if request.method == 'GET':
        return render_template('add.html')

    # Because we 'returned' for a 'GET', if we get to this next bit, we must
    # have received a POST

    # Get the incoming data from the request.form dictionary.
    # The values on the right, inside get(), correspond to the 'name'
    # values in the HTML form that was submitted.

    # user_price = request.form.get('price_field')
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    user = create_user(name=name, email=email, password=password)
    return render_template('add.html', user=user)
