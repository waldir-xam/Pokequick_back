from flask_restx import fields
from flask_restx.reqparse import RequestParser
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow.fields import Nested
from app.models.pokemon_model import PokemonModel


class PokemonRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def all(self):
        parser = RequestParser()
        parser.add_argument('page', type=int, default=1, location='args')
        parser.add_argument('per_page', type=int, default=5, location='args')
        return parser

    def create(self):
        return self.namespace.model('Pokemon Create', {
            'nombre': fields.String(required=True, min_length=4, max_length=80),
            'tipo': fields.String(required=True, min_length=3, max_length=80),
            'vida': fields.String(required=True, min_length=3, max_length=80),
            'ataque': fields.String(required=True, min_length=3, max_length=80),
            'defensa': fields.String(required=True, min_length=3, max_length=80),
            'especialidad': fields.String(required=True, min_length=3, max_length=80),
            'foto': fields.String(required=True, min_length=4, max_length=250)
        })

    def update(self):
        return self.namespace.model('Pokemon Update', {
            'nombre': fields.String(required=False, min_length=4, max_length=80),
            'tipo': fields.String(required=False, min_length=3, max_length=80),
            'vida': fields.String(required=False, min_length=3, max_length=80),
            'ataque': fields.String(required=False, min_length=3, max_length=80),
            'defensa': fields.String(required=False, min_length=3, max_length=80),
            'especialidad': fields.String(required=False, min_length=3, max_length=80),
            'foto': fields.String(required=False, min_length=4, max_length=250)
        })


class PokemonResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = PokemonModel
        ordered = True

    coleccion = Nested('ColeccionResponseSchema', many=True)
