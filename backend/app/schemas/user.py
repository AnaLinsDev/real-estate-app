from datetime import datetime
from pydantic import BaseModel, EmailStr


# ---------------------------------------------------
# Base – campos comuns usados em múltiplos schemas
# ---------------------------------------------------
class UserBase(BaseModel):
    username: str
    email: EmailStr


# ---------------------------------------------------
# Create – usado no registro, inclui a senha
# ---------------------------------------------------
class UserCreate(UserBase):
    password: str


# ---------------------------------------------------
# Read – representa o que será retornado pela API
# (não retorna a senha)
# ---------------------------------------------------
class UserRead(UserBase):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True  # para funcionar com Prisma ORM objects


# ---------------------------------------------------
# Login – payload enviado para /login
# ---------------------------------------------------
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# ---------------------------------------------------
# JWT Token response
# ---------------------------------------------------
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
