from sqlalchemy.orm import Session
from app.models.empresa import Empresa
from app.schemas.empresa import EmpresaUpdate
from app.utils import a_mayusculas

def get_empresa(db: Session):
    return db.query(Empresa).first()

def update_empresa(db: Session, data: EmpresaUpdate):
    db_empresa = get_empresa(db)
    if not db_empresa:
        db_empresa = Empresa()
        db.add(db_empresa)
    db_empresa.nombre = a_mayusculas(data.nombre)
    db_empresa.razon_social = a_mayusculas(data.razon_social)
    db_empresa.nit = a_mayusculas(data.nit)
    db_empresa.telefono = a_mayusculas(data.telefono)
    db_empresa.correo = data.correo
    db_empresa.direccion = a_mayusculas(data.direccion)
    db_empresa.ciudad = a_mayusculas(data.ciudad)
    db_empresa.color_principal = data.color_principal
    db_empresa.color_secundario = data.color_secundario
    db.commit()
    db.refresh(db_empresa)
    return db_empresa
