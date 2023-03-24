from os import getenv
from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from config import enviroment

app = Flask(__name__)
CORS(app)
app.config.from_object(enviroment[getenv("ENVIRONMENT")])

authorizations = {"Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}}

api = Api(
    app,
    title="Bolerplate Poke Collect",
    version="0.1",
    description="Endpoints del boilerplate",
    authorizations=authorizations,
    doc="/swagger-ui",
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
