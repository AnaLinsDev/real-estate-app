from datetime import datetime
from pydantic import BaseModel
from typing import Optional


# ---------------------------------------------------
# Base – campos usados em Create e Read
# ---------------------------------------------------
class PropertyBase(BaseModel):
    name: str
    type: str
    address: Optional[str] = None
    status: str = "available"
    photos: Optional[str] = None   # armazenado como texto (JSON string)
    notes: Optional[str] = None


# ---------------------------------------------------
# Create – usado no cadastro de propriedades
# ---------------------------------------------------
class PropertyCreate(PropertyBase):
    pass  # nenhum campo adicional além dos do Base


# ---------------------------------------------------
# Read – resposta da API (inclui id)
# ---------------------------------------------------
class PropertyRead(PropertyBase):
    id: int

    class Config:
        from_attributes = True
