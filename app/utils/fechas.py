from datetime import datetime
from typing import Optional
from zoneinfo import ZoneInfo

# Zona horaria oficial del sistema (Bolivia, sin horario de verano: -04:00)
TIME_ZONE = ZoneInfo("America/La_Paz")
DB_OFFSET = "-04:00"


def ahora_local() -> datetime:
    """Fecha/hora actual en America/La_Paz, naive (sin tzinfo) para guardar en MySQL."""
    return datetime.now(TIME_ZONE).replace(tzinfo=None)


def formatear_fecha(fecha: datetime, formato: str = "%Y-%m-%d") -> str:
    if not fecha:
        return ""
    return fecha.strftime(formato)

def parse_fecha(fecha_str: str, formato: str = "%Y-%m-%d") -> Optional[datetime]:
    if not fecha_str:
        return None
    return datetime.strptime(fecha_str, formato)

def obtener_inicio_dia(fecha: datetime) -> datetime:
    return fecha.replace(hour=0, minute=0, second=0, microsecond=0)

def obtener_fin_dia(fecha: datetime) -> datetime:
    return fecha.replace(hour=23, minute=59, second=59, microsecond=999999)
