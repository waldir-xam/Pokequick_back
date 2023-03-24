from app import db
from app.models.coleccion_model import ColeccionModel
from app.schemas.coleccion_schemas import ColeccionResponseSchema
from flask_jwt_extended import current_user

class ColeccionController:
    def __init__(self):
        self.model = ColeccionModel
        self.schema = ColeccionResponseSchema

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
                'message': 'ocurrio un error',
                'error': str(e)
            }, 500
            

    def getById(self, id):
        try:
            record = self.model.where(id=id).first()
            if record:

                response = self.schema(many=False)
                return response.dump(record), 200
                

            return {
                 'message': 'no se encontro la coleccion',
                 
            }, 500
        except Exception as e:
            return {
                'message': 'ocurrio un error',
                'error': str(e)
            }, 500
    def create(self, data):
        try:
            new_record = self.model.create(**data)
            db.session.add(new_record)
            db.session.commit()
            return {
                'message': f'el rol {data["usuario_id"]} se creo con exito'
            }, 201
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'ocurrio un error',
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
                    'message': f'El rol {id} fue actualizado'
                }, 200
            return {
                'message': 'no se encontro el rol'
            }, 404
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'ocurrio un error',
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
                    'message': f'El rol {id} fue deshabilitado'
                }, 200
            return {
                'message': 'no se encontro el rol'
            }, 404
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'ocurrio un error',
                'error': str(e)
            }, 500
