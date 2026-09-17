from sqlalchemy import Column, Integer, DateTime
from app.database import Base
from app.utils.fechas import ahora_local

class BaseModel(Base):
    __abstract__ = True
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha_registro = Column(DateTime, default=ahora_local)
    fecha_actualizado = Column(DateTime, default=ahora_local, onupdate=ahora_local)
