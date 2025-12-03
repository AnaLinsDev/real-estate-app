from fastapi import APIRouter, Depends, HTTPException
from prisma import Prisma
from app.database.database import get_db
from app.schemas.tenant import TenantCreate, TenantRead, TenantUpdate

router = APIRouter()


# -------------------------------------------------------
# CREATE
# -------------------------------------------------------
@router.post("/", response_model=TenantRead)
async def create_tenant(data: TenantCreate, db: Prisma = Depends(get_db)):
    new_tenant = await db.tenant.create(
        data=data.model_dump()
    )
    return new_tenant


# -------------------------------------------------------
# READ ALL
# -------------------------------------------------------
@router.get("/", response_model=list[TenantRead])
async def list_tenants(db: Prisma = Depends(get_db)):
    tenants = await db.tenant.find_many()
    return tenants


# -------------------------------------------------------
# READ ONE
# -------------------------------------------------------
@router.get("/{tenant_id}", response_model=TenantRead)
async def get_tenant(tenant_id: int, db: Prisma = Depends(get_db)):
    tenant = await db.tenant.find_unique(where={"id": tenant_id})

    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")

    return tenant


# -------------------------------------------------------
# UPDATE
# -------------------------------------------------------
@router.put("/{tenant_id}", response_model=TenantRead)
async def update_tenant(
    tenant_id: int,
    data: TenantUpdate,
    db: Prisma = Depends(get_db),
):
    existing = await db.tenant.find_unique(where={"id": tenant_id})

    if not existing:
        raise HTTPException(status_code=404, detail="Tenant not found")

    updated = await db.tenant.update(
        where={"id": tenant_id},
        data=data.model_dump(exclude_unset=True)
    )
    return updated


# -------------------------------------------------------
# DELETE
# -------------------------------------------------------
@router.delete("/{tenant_id}")
async def delete_tenant(tenant_id: int, db: Prisma = Depends(get_db)):
    existing = await db.tenant.find_unique(where={"id": tenant_id})

    if not existing:
        raise HTTPException(status_code=404, detail="Tenant not found")

    await db.tenant.delete(where={"id": tenant_id})

    return {"detail": "Tenant deleted successfully"}
