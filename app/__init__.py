import redis
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ccna_user:ccna_password@db/ccna_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis.Redis(host='redis', port=6379)
Session(app)

metrics = PrometheusMetrics(app)
# Set a secret key for session management
app.config['SECRET_KEY'] = 'adi2603'  # Replace with a secure, random key

db = SQLAlchemy(app)

from app import routes, models
