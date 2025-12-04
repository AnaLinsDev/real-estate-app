from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional
from app.schemas.property_photo import PropertyPhotoRead

# ---------------------------------------------------
# Base – campos usados em Create e Read
# ---------------------------------------------------
class PropertyBase(BaseModel):
    name: str
    type: str
    address: Optional[str] = None
    status: str = "available"
    photos: Optional[str] = None   # JSON armazenado como texto
    notes: Optional[str] = None


# ---------------------------------------------------
# Create – entrada ao criar uma propriedade
# ---------------------------------------------------
class PropertyCreate(PropertyBase):
    pass


# ---------------------------------------------------
# Update – permite atualizar parcialmente
# ---------------------------------------------------
class PropertyUpdate(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    address: Optional[str] = None
    status: Optional[str] = None
    photos: Optional[str] = None
    notes: Optional[str] = None


# ---------------------------------------------------
# Read – resposta da API (inclui id)
# ---------------------------------------------------
class PropertyRead(BaseModel):
    id: int
    name: str
    type: str
    address: str | None
    status: str
    notes: str | None
    property_photos: list[PropertyPhotoRead] = []

    class Config:
        from_attributes = True

