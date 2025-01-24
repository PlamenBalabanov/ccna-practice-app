from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ccna_user:ccna_password@db/ccna_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set a secret key for session management
app.config['SECRET_KEY'] = 'adi2603'  # Replace with a secure, random key

db = SQLAlchemy(app)

from app import routes, models
