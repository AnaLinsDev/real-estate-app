from pydantic import BaseModel, EmailStr
from typing import Optional


# ---------------------------------------------------
# Base – campos principais (usado em Create e Read)
# ---------------------------------------------------
class TenantBase(BaseModel):
    name: str
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    documents: Optional[str] = None   # JSON armazenado como texto
    notes: Optional[str] = None


# ---------------------------------------------------
# Create – usado ao cadastrar um novo inquilino
# ---------------------------------------------------
class TenantCreate(TenantBase):
    pass  # nenhum campo extra além dos do Base


# ---------------------------------------------------
# Read – resposta da API com o ID
# ---------------------------------------------------
class TenantRead(TenantBase):
    id: int

    class Config:
        from_attributes = True
