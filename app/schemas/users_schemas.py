from flask_restx import fields
from flask_restx.reqparse import RequestParser
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow.fields import Nested
from app.models.users_model import UserModel


class UserRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def all(self):
        parser = RequestParser()
        parser.add_argument('page', type=int, default=1, location='args')
        parser.add_argument('per_page', type=int, default=5, location='args')
        return parser

    def create(self):
        return self.namespace.model('Auth Signup', {
            'usuario': fields.String(required=True, min_length=4, max_length=80),
            'correo': fields.String(required=True, min_length=5, max_length=80),
            'contrasena': fields.String(required=True, min_length=4, max_length=120),
            'rol_id': fields.Integer(required=True)
        })

    def update(self):
        return self.namespace.model('User Update', {
            'usuario': fields.String(required=False, min_length=4, max_length=80),
            'correo': fields.String(required=False, min_length=5, max_length=80),
            'contrasena': fields.String(required=False, min_length=4, max_length=120),
            'rol_id': fields.Integer(required=False)
        })


class UsersResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        ordered = True
        exclude = ['contrasena']

    coleccion = Nested('ColeccionResponseSchema', many=True)