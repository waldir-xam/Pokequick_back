from app.models.base import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from bcrypt import hashpw, gensalt, checkpw

from sqlalchemy.orm import relationship

class UserModel(BaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)

    usuario = Column(String(80), unique=True)
    correo = Column(String(80), unique=True)
    contrasena = Column(String(120), nullable=False)

    estado = Column(Boolean, default=True)

    rol_id = Column(Integer, ForeignKey('roles.id'))

    coleccion = relationship('ColeccionModel', uselist=True, back_populates='user')


    def hashContrasena(self):
        pwd_encode = self.contrasena.encode('utf-8')
        pwd_hash = hashpw(pwd_encode, gensalt(rounds=10))
        self.contrasena = pwd_hash.decode('utf-8')

    def checkContrasena(self, contrasena):
        return checkpw(
            contrasena.encode('utf-8'),
            self.contrasena.encode('utf-8')
        )
