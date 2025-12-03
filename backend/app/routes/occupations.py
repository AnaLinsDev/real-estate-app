from fastapi import APIRouter, Depends, HTTPException
from prisma import Prisma
from app.database.database import get_db
from app.schemas.occupation import (
    OccupationCreate,
    OccupationUpdate,
    OccupationRead,
)

router = APIRouter()


# -------------------------------------------------------
# CREATE
# -------------------------------------------------------
@router.post("/", response_model=OccupationRead)
async def create_occupation(data: OccupationCreate, db: Prisma = Depends(get_db)):
    new_occ = await db.occupation.create(
        data=data.model_dump()
    )
    return new_occ


# -------------------------------------------------------
# READ ALL
# -------------------------------------------------------
@router.get("/", response_model=list[OccupationRead])
async def list_occupations(db: Prisma = Depends(get_db)):
    occs = await db.occupation.find_many()
    return occs


# -------------------------------------------------------
# READ ONE
# -------------------------------------------------------
@router.get("/{occupation_id}", response_model=OccupationRead)
async def get_occupation(occupation_id: int, db: Prisma = Depends(get_db)):
    occ = await db.occupation.find_unique(where={"id": occupation_id})

    if not occ:
        raise HTTPException(status_code=404, detail="Occupation not found")

    return occ


# -------------------------------------------------------
# UPDATE
# -------------------------------------------------------
@router.put("/{occupation_id}", response_model=OccupationRead)
async def update_occupation(
    occupation_id: int,
    data: OccupationUpdate,
    db: Prisma = Depends(get_db),
):
    existing = await db.occupation.find_unique(where={"id": occupation_id})

    if not existing:
        raise HTTPException(status_code=404, detail="Occupation not found")

    updated = await db.occupation.update(
        where={"id": occupation_id},
        data=data.model_dump(exclude_unset=True)
    )
    return updated


# -------------------------------------------------------
# DELETE
# -------------------------------------------------------
@router.delete("/{occupation_id}")
async def delete_occupation(occupation_id: int, db: Prisma = Depends(get_db)):
    existing = await db.occupation.find_unique(where={"id": occupation_id})

    if not existing:
        raise HTTPException(status_code=404, detail="Occupation not found")

    await db.occupation.delete(where={"id": occupation_id})

    return {"detail": "Occupation deleted successfully"}
