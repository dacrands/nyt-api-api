from flask import Flask
from config import Config
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
jwt = JWTManager(app)

from app import routes, models

