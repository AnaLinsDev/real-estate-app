from sqlmodel import SQLModel
from typing import Optional
from pydantic import BaseModel

class PropertyPhotoBase(BaseModel):
    property_id: int

class PropertyPhotoCreate(PropertyPhotoBase):
    pass

class PropertyPhotoRead(PropertyPhotoBase):
    id: int
    url_photo: str

    class Config:
        from_attributes = True
