from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

app = Flask(__name__)

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_PATH
app.config['DB_PATH'] = config.DB_PATH

if __name__ == "__main__":
    from views import *
    app.run(debug=True, port=5000)
