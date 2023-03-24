from app.models.base import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from bcrypt import hashpw, gensalt, checkpw
from sqlalchemy.orm import relationship


class ColeccionModel(BaseModel):
    __tablename__ = 'coleccion'

    id = Column(Integer, primary_key=True, autoincrement=True)

    usuario_id = Column(Integer, ForeignKey('users.id'))
    pokemon_id = Column(Integer, ForeignKey('pokemon.id'))
    estado = Column(Boolean, default=True)
    
    user = relationship('UserModel', uselist=True, back_populates='coleccion')

    pokemon = relationship('PokemonModel', uselist=True, back_populates='coleccion')

