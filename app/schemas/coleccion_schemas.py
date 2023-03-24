from flask_restx import fields
from flask_restx.reqparse import RequestParser
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow.fields import Nested
from app.models.coleccion_model import ColeccionModel


class ColeccionRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def all(self):
        parser = RequestParser()
        parser.add_argument('page', type=int, default=1, location='args')
        parser.add_argument('per_page', type=int, default=5, location='args')
        return parser

    def create(self):
        return self.namespace.model('crear Coleccion', {
            #'name': fields.String(required=True, max_lenght=80),
            'usuario_id': fields.Integer(required=True),
            'pokemon_id': fields.Integer(required=True)
        })

    def update(self):
        return self.namespace.model('Actualizar Coleccion', {
            #'name': fields.String(required=True, max_lenght=80)
            'usuario_id': fields.Integer(required=True),
            'pokemon_id': fields.Integer(required=True)
        })


class ColeccionResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ColeccionModel
        ordered = True

    users = Nested('UsersResponseSchema', exclude=['coleccion'], many=True)
    pokemon = Nested('PokemonResponseSchema', exclude=['coleccion'], many=True)