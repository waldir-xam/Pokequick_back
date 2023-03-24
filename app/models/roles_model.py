from app.models.base import BaseModel
from sqlalchemy import Column, Integer, String, Boolean


class RoleModel(BaseModel):
    # nombre tabla
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80))
    status = Column(Boolean, default=True)
