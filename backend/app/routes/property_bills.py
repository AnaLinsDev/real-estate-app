from fastapi import APIRouter, Depends, HTTPException
from prisma import Prisma

from app.database.database import get_db
from app.schemas.property_bill import (
    PropertyBillCreate,
    PropertyBillRead,
    PropertyBillUpdate,
)

router = APIRouter()


# ------------------------------------------------
# CREATE
# ------------------------------------------------
@router.post("/", response_model=PropertyBillRead)
async def create_property_bill(
    data: PropertyBillCreate,
    db: Prisma = Depends(get_db)
):
    bill = await db.propertybill.create(
        data=data.model_dump()
    )
    return bill


# ------------------------------------------------
# READ ALL
# ------------------------------------------------
@router.get("/", response_model=list[PropertyBillRead])
async def list_property_bills(
    db: Prisma = Depends(get_db)
):
    return await db.propertybill.find_many()


# ------------------------------------------------
# READ ONE
# ------------------------------------------------
@router.get("/{bill_id}", response_model=PropertyBillRead)
async def get_property_bill(
    bill_id: int,
    db: Prisma = Depends(get_db)
):
    bill = await db.propertybill.find_unique(
        where={"id": bill_id}
    )

    if not bill:
        raise HTTPException(
            status_code=404,
            detail="Property Bill not found"
        )

    return bill


# ------------------------------------------------
# UPDATE
# ------------------------------------------------
@router.patch("/{bill_id}", response_model=PropertyBillRead)
async def update_property_bill(
    bill_id: int,
    data: PropertyBillUpdate,
    db: Prisma = Depends(get_db)
):
    exists = await db.propertybill.find_unique(
        where={"id": bill_id}
    )

    if not exists:
        raise HTTPException(
            status_code=404,
            detail="Property Bill not found"
        )

    bill = await db.propertybill.update(
        where={"id": bill_id},
        data=data.model_dump(exclude_unset=True)
    )

    return bill


# ------------------------------------------------
# DELETE
# ------------------------------------------------
@router.delete("/{bill_id}")
async def delete_property_bill(
    bill_id: int,
    db: Prisma = Depends(get_db)
):
    exists = await db.propertybill.find_unique(
        where={"id": bill_id}
    )

    if not exists:
        raise HTTPException(
            status_code=404,
            detail="Property Bill not found"
        )

    await db.propertybill.delete(
        where={"id": bill_id}
    )

    return {"detail": "Property Bill deleted successfully"}
