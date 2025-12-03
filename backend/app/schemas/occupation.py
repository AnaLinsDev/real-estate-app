from typing import Optional
from sqlmodel import SQLModel


# ------------------------------
# Base
# ------------------------------
class OccupationBase(SQLModel):
    property_id: int
    tenant_id: int
    start_date: str   # ISO string
    end_date: Optional[str] = None
    notes: Optional[str] = None


# ------------------------------
# Create
# ------------------------------
class OccupationCreate(OccupationBase):
    pass


# ------------------------------
# Read
# ------------------------------
class OccupationRead(OccupationBase):
    id: int
