from app import api
from flask_restx import Resource
from flask import request
from app.controllers.pokemon_controller import PokemonController
from app.schemas.pokemon_schemas import PokemonRequestSchema
from flask_jwt_extended import jwt_required


pokemon_ns = api.namespace(
    name='Pokemon',
    description='Rutas del modulo Pokemon',
    path='/pokemon'
)

request_schema = PokemonRequestSchema(pokemon_ns)


@pokemon_ns.route('')
@pokemon_ns.doc(security='Bearer')
class Pokemons(Resource):
    @jwt_required()
    @pokemon_ns.expect(request_schema.all())
    def get(self):
        ''' Listar Pokemons '''
        query = request_schema.all().parse_args()
        controller = PokemonController()
        return controller.all(query)

    @jwt_required()
    @pokemon_ns.expect(request_schema.create(), validate=True)
    def post(self):
        ''' Crear Pokemon '''
        controller = PokemonController()
        return controller.create(request.json)


@pokemon_ns.route('/<int:id>')
@pokemon_ns.doc(security='Bearer')
class PokemonById(Resource):
    @jwt_required()
    def get(self, id):
        ''' Obtener Pokemon por ID '''
        controller = PokemonController()
        return controller.getById(id)

    @jwt_required()
    @pokemon_ns.expect(request_schema.update(), validate=True)
    def put(self, id):
        ''' Actualizar Pokemon por ID '''
        controller = PokemonController()
        return controller.update(id, request.json)

    @jwt_required()
    def delete(self, id):
        ''' Inhabilitar Pokemon por ID '''
        controller = PokemonController()
        return controller.delete(id)
