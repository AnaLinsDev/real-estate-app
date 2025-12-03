from fastapi import APIRouter, Depends, HTTPException
from prisma import Prisma

from app.database.database import get_db
from app.schemas.property_investment import (
    PropertyInvestmentCreate,
    PropertyInvestmentRead,
    PropertyInvestmentUpdate,
)

router = APIRouter()


# ------------------------------------------------
# CREATE
# ------------------------------------------------
@router.post("/", response_model=PropertyInvestmentRead)
async def create_property_investment(
    data: PropertyInvestmentCreate,
    db: Prisma = Depends(get_db)
):
    investment = await db.propertyinvestment.create(
        data=data.model_dump()
    )
    return investment


# ------------------------------------------------
# READ ALL
# ------------------------------------------------
@router.get("/", response_model=list[PropertyInvestmentRead])
async def list_property_investments(
    db: Prisma = Depends(get_db)
):
    return await db.propertyinvestment.find_many()


# ------------------------------------------------
# READ ONE
# ------------------------------------------------
@router.get("/{investment_id}", response_model=PropertyInvestmentRead)
async def get_property_investment(
    investment_id: int,
    db: Prisma = Depends(get_db)
):
    investment = await db.propertyinvestment.find_unique(
        where={"id": investment_id}
    )

    if not investment:
        raise HTTPException(
            status_code=404,
            detail="Property Investment not found"
        )

    return investment


# ------------------------------------------------
# UPDATE (PARTIAL)
# ------------------------------------------------
@router.patch("/{investment_id}", response_model=PropertyInvestmentRead)
async def update_property_investment(
    investment_id: int,
    data: PropertyInvestmentUpdate,
    db: Prisma = Depends(get_db)
):
    exists = await db.propertyinvestment.find_unique(
        where={"id": investment_id}
    )

    if not exists:
        raise HTTPException(
            status_code=404,
            detail="Property Investment not found"
        )

    investment = await db.propertyinvestment.update(
        where={"id": investment_id},
        data=data.model_dump(exclude_unset=True)
    )

    return investment


# ------------------------------------------------
# DELETE
# ------------------------------------------------
@router.delete("/{investment_id}")
async def delete_property_investment(
    investment_id: int,
    db: Prisma = Depends(get_db)
):
    exists = await db.propertyinvestment.find_unique(
        where={"id": investment_id}
    )

    if not exists:
        raise HTTPException(
            status_code=404,
            detail="Property Investment not found"
        )

    await db.propertyinvestment.delete(
        where={"id": investment_id}
    )

    return {"detail": "Property Investment deleted successfully"}
