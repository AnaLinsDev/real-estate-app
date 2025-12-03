from fastapi import APIRouter, Depends, HTTPException
from prisma import Prisma
from app.database.database import get_db
from app.schemas.user import UserLogin
from app.utils.hashing import verify_password
from app.utils.security import create_token

router = APIRouter()

@router.post("/login")
async def login(data: UserLogin, db: Prisma = Depends(get_db)):
    user = await db.user.find_unique(where={"email": data.email})

    if not user or not verify_password(data.password, user.hashedPassword):
        raise HTTPException(400, "Incorrect credentials")

    token = create_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}
