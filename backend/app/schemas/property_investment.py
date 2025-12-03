from pydantic import BaseModel
from typing import Optional


# ---------------------------------------------------
# Base – campos principais
# ---------------------------------------------------
class PropertyInvestmentBase(BaseModel):
    property_id: int
    description: str
    reference_month: str   # YYYY-MM
    date: str              # YYYY-MM-DD
    amount: float
    notes: Optional[str] = None


# ---------------------------------------------------
# Create – usado ao cadastrar um investimento
# ---------------------------------------------------
class PropertyInvestmentCreate(PropertyInvestmentBase):
    pass


# ---------------------------------------------------
# Update – PATCH (todos opcionais)
# ---------------------------------------------------
class PropertyInvestmentUpdate(BaseModel):
    property_id: Optional[int] = None
    description: Optional[str] = None
    reference_month: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[float] = None
    notes: Optional[str] = None


# ---------------------------------------------------
# Read – resposta da API
# ---------------------------------------------------
class PropertyInvestmentRead(PropertyInvestmentBase):
    id: int

    class Config:
        from_attributes = True
