from app.models.base import BaseModel
from sqlalchemy import Column, Integer, String, Boolean

from sqlalchemy.orm import relationship


class PokemonModel(BaseModel):
    __tablename__ = 'pokemon'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(80), unique=True)
    tipo = Column(String(80))
    vida = Column(String(80))
    ataque = Column(String(80))
    defensa = Column(String(80))
    especialidad = Column(String(80))
    foto = Column(String(250))
    estado = Column(Boolean, default=True)

    coleccion = relationship('ColeccionModel', uselist=True, back_populates='pokemon')