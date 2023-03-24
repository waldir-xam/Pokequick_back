from app import api
from flask import request
from flask_restx import Resource
from app.schemas.auth_schemas import AuthRequestSchema
from app.controllers.auth_controller import AuthController
from flask_jwt_extended import jwt_required, get_jwt_identity

auth_ns = api.namespace(
    name='Autenticación',
    description='Rutas del modelo de autenticación',
    path='/auth'
)

request_schema = AuthRequestSchema(auth_ns)


@auth_ns.route('/signin')
class SignIn(Resource):
    @auth_ns.expect(request_schema.signin(), validate=True)
    def post(self):
        ''' Login de usuario '''
        controller = AuthController()
        return controller.signIn(request.json)


@auth_ns.route('/signup')
class SignUp(Resource):
    @auth_ns.expect(request_schema.signup(), validate=True)
    def post(self):
        '''Registrar Usuario'''
        controller = AuthController()
        return controller.signUp(request.json)
