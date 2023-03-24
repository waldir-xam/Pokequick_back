from app import api
from flask import request
from flask_restx import Resource
from app.controllers.coleccion_controller import ColeccionController
from app.schemas.coleccion_schemas import ColeccionRequestSchema

coleccion_ns = api.namespace(
    name='Coleccion',
    description='Rutas del modelo de Coleccion',
    path='/coleccion'
)

request_schema = ColeccionRequestSchema(coleccion_ns)


@coleccion_ns.route('')
class Coleccion(Resource):
    @coleccion_ns.expect(request_schema.all())
    def get(self):
        '''Listar las colecciones'''
        query = request_schema.all().parse_args()
        controller = ColeccionController()
        return controller.all(query)

    @coleccion_ns.expect(request_schema.create(), validate=True)
    def post(self):
        '''Crear Coleccion'''
        controller = ColeccionController()
        return controller.create(request.json)


@coleccion_ns.route('/Coleccion/<int:id>')
class ColeccionById(Resource):
    def get(self, id):
        '''Obtener coleccion por id'''
        controller = ColeccionController()
        return controller.getById(id)

    @coleccion_ns.expect(request_schema.update(), validate=True)
    def put(self, id):
        '''Actualizar coleccion por id'''
        controller = ColeccionController()
        return controller.update(id, request.json)

    def delete(self, id):
        '''Eliminar coleccion por id'''
        controller = ColeccionController()
        return controller.delete(id)