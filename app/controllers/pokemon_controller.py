from app import db
from app.models.pokemon_model import PokemonModel
from app.schemas.pokemon_schemas import PokemonResponseSchema
from flask_jwt_extended import current_user


class PokemonController:

    def __init__(self):
        self.model = PokemonModel
        self.schema = PokemonResponseSchema
        self.current_user = current_user

    def all(self, query):
        try:
            page = query['page']
            per_page = query['per_page']

            records = self.model.where(estado=True).order_by('id').paginate(
                page=page, per_page=per_page
            )

            response = self.schema(many=True)

            return {
                'results': response.dump(records.items),
                'pagination': {
                    'totalRecords': records.total,
                    'totalPages': records.pages,
                    'perPage': records.per_page,
                    'currentPage': records.page
                }
            }, 200
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500

    def create(self, data):
        try:
            new_record = self.model.create(**data)
            db.session.add(new_record)
            db.session.commit()
            return {
                'message': 'Pokemon creado con exito'
            }, 201
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500

    def getById(self, id):
        try:
            record = self.model.where(id=id).first()
            if record:
                response = self.schema(many=False)
                return response.dump(record), 200
            return {
                'message': 'No se encontro el Pokemon'
            }, 404
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500

    def update(self, id, data):
        try:
            record = self.model.where(id=id).first()
            if record:
                record.update(**data)
                db.session.add(record)
                db.session.commit()
                return {
                    'message': f'Pokemon {id}, fue actualizado'
                }, 200
            return {
                'message': 'No se encontro el pokemon mencionado'
            }, 404
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500

    def delete(self, id):
        try:
            record = self.model.where(id=id).first()
            if record and record.estado:
                record.update(estado=False)
                db.session.add(record)
                db.session.commit()
                return {
                    'message': f'Pokemon {id}, fue deshabilitado'
                }, 200
            return {
                'message': 'No se encontro el pokemon mencionado'
            }, 404
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500
