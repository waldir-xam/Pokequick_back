from flask_restx import fields


class AuthRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def signin(self):
        return self.namespace.model('Auth SignIn', {
            'usuario': fields.String(required=True),
            'contrasena': fields.String(required=True)
        })

    def signup(self):
        return self.namespace.model('Auth Signup', {
            'usuario': fields.String(required=True, min_length=4, max_length=80),
            'correo': fields.String(required=True, min_length=5, max_length=80),
            'contrasena': fields.String(required=True, min_length=4, max_length=120)
        })
