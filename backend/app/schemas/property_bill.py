from typing import Optional
from sqlmodel import SQLModel


# ------------------------------
# Base
# ------------------------------
class PropertyBillBase(SQLModel):
    property_id: int
    tenant_id: Optional[int] = None
    bill_type: str
    reference_month: str    # YYYY-MM
    due_date: Optional[str] = None
    paid_date: Optional[str] = None
    amount: float
    notes: Optional[str] = None


# ------------------------------
# Create
# ------------------------------
class PropertyBillCreate(PropertyBillBase):
    pass


# ------------------------------
# Read
# ------------------------------
class PropertyBillRead(PropertyBillBase):
    id: int
