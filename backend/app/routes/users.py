from fastapi import APIRouter, Depends, HTTPException
from prisma import Prisma
from app.database.database import get_db
from app.schemas.user import UserCreate, UserRead
from app.utils.hashing import hash_password

router = APIRouter()

@router.post("/", response_model=UserRead)
async def create_user(data: UserCreate, db: Prisma = Depends(get_db)):
    exists = await db.user.find_unique(where={"email": data.email})
    if exists:
        raise HTTPException(400, "Email already registered")

    user = await db.user.create({
        "username": data.username,
        "email": data.email,
        "hashedPassword": hash_password(data.password)
    })

    return user
