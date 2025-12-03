from typing import Optional
from sqlmodel import SQLModel


# ------------------------------
# Base
# ------------------------------
class PropertyInvestmentBase(SQLModel):
    property_id: int
    description: str
    reference_month: str   # YYYY-MM
    date: str              # YYYY-MM-DD
    amount: float
    notes: Optional[str] = None


# ------------------------------
# Create
# ------------------------------
class PropertyInvestmentCreate(PropertyInvestmentBase):
    pass


# ------------------------------
# Read
# ------------------------------
class PropertyInvestmentRead(PropertyInvestmentBase):
    id: int
