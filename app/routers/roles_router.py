from app import api
from flask import request
from flask_restx import Resource
from app.controllers.roles_controller import RolesController
from app.schemas.roles_schemas import RolesRequestSchema

role_ns = api.namespace(
    name='Roles',
    description='Rutas del modelo de roles',
    path='/roles'
)

request_schema = RolesRequestSchema(role_ns)


@role_ns.route('')
class Roles(Resource):
    @role_ns.expect(request_schema.all())
    def get(self):
        '''Listar los roles'''
        query = request_schema.all().parse_args()
        controller = RolesController()
        return controller.all(query)

    @role_ns.expect(request_schema.create(), validate=True)
    def post(self):
        '''Crear rol'''
        controller = RolesController()
        return controller.create(request.json)


@role_ns.route('/roles/<int:id>')
class RolesById(Resource):
    def get(self, id):
        '''Obtener rol id'''
        controller = RolesController()
        return controller.getById(id)

    @role_ns.expect(request_schema.update(), validate=True)
    def put(self, id):
        '''Actualizar rol id'''
        controller = RolesController()
        return controller.update(id, request.json)

    def delete(self, id):
        '''Eliminar rol id'''
        controller = RolesController()
        return controller.delete(id)
