from pydantic import BaseModel
from typing import Optional


class OccupationBase(BaseModel):
    property_id: int
    tenant_id: int
    start_date: str     # ISO string
    end_date: Optional[str] = None
    notes: Optional[str] = None


class OccupationCreate(OccupationBase):
    pass


class OccupationUpdate(BaseModel):
    property_id: Optional[int] = None
    tenant_id: Optional[int] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    notes: Optional[str] = None


class OccupationRead(OccupationBase):
    id: int

    class Config:
        from_attributes = True
