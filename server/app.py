from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['DB_PATH'] = 'sqlite:///database.db'

if __name__ == "__main__":
    from views import *
    app.run(debug=True, port=5000)
