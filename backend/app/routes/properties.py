import os
from fastapi import APIRouter, Depends, HTTPException
from prisma import Prisma
from app.database.database import get_db
from app.schemas.property import PropertyCreate, PropertyRead, PropertyUpdate


router = APIRouter()


# -------------------------------------------------------
# CREATE
# -------------------------------------------------------
@router.post("/", response_model=PropertyRead)
async def create_property(data: PropertyCreate, db: Prisma = Depends(get_db)):
    new_property = await db.property.create(
        data=data.model_dump()
    )
    return new_property



# -------------------------------------------------------
# GET ALL
# -------------------------------------------------------
@router.get("/", response_model=list[PropertyRead])
async def list_properties(db: Prisma = Depends(get_db)):
    properties = await db.property.find_many(
        include={"property_photos": True}
    )
    return properties


# -------------------------------------------------------
# GET ONE
# -------------------------------------------------------
@router.get("/{property_id}", response_model=PropertyRead)
async def get_property(property_id: int, db: Prisma = Depends(get_db)):
    property_db = await db.property.find_unique(
        where={"id": property_id},
        include={"property_photos": True}
    )

    if not property_db:
        raise HTTPException(status_code=404, detail="Property not found")

    return property_db


# -------------------------------------------------------
# UPDATE
# -------------------------------------------------------
@router.put("/{property_id}", response_model=PropertyRead)
async def update_property(
    property_id: int,
    data: PropertyUpdate,
    db: Prisma = Depends(get_db)
):
    # verify exists
    existing = await db.property.find_unique(where={"id": property_id})
    if not existing:
        raise HTTPException(status_code=404, detail="Property not found")

    updated = await db.property.update(
        where={"id": property_id},
        data=data.model_dump(exclude_unset=True)
    )
    return updated


# -------------------------------------------------------
# DELETE
# -------------------------------------------------------
@router.delete("/{property_id}")
async def delete_property(property_id: int, db: Prisma = Depends(get_db)):
    existing = await db.property.find_unique(where={"id": property_id})

    if not existing:
        raise HTTPException(status_code=404, detail="Property not found")

    await db.property.delete(where={"id": property_id})

    return {"detail": "Property deleted successfully"}
