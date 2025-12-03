# app/schemas/property_bill.py
from typing import Optional
from sqlmodel import SQLModel


class PropertyBillBase(SQLModel):
    property_id: int
    tenant_id: Optional[int] = None
    bill_type: str
    reference_month: str  # YYYY-MM
    due_date: Optional[str] = None
    paid_date: Optional[str] = None
    amount: float
    notes: Optional[str] = None


class PropertyBillCreate(PropertyBillBase):
    pass


class PropertyBillRead(PropertyBillBase):
    id: int


class PropertyBillUpdate(SQLModel):
    property_id: Optional[int] = None
    tenant_id: Optional[int] = None
    bill_type: Optional[str] = None
    reference_month: Optional[str] = None
    due_date: Optional[str] = None
    paid_date: Optional[str] = None
    amount: Optional[float] = None
    notes: Optional[str] = None
