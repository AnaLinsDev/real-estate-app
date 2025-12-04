import os
from fastapi import APIRouter, HTTPException, Depends, UploadFile, File
from typing import List
from prisma import Prisma
from app.database.database import get_db
from fastapi.responses import FileResponse


router = APIRouter()

UPLOAD_DIR = "uploads"
MAX_PHOTOS = 10


@router.post("/upload/{property_id}")
async def upload_photos(
    property_id: int,
    files: List[UploadFile] = File(...),
    db: Prisma = Depends(get_db)
):

    # Verifica quantas fotos já existem para este imóvel
    existing_photos = await db.propertyphoto.find_many(
        where={"property_id": property_id}
    )

    if len(existing_photos) + len(files) > MAX_PHOTOS:
        raise HTTPException(
            status_code=400,
            detail=f"Você pode enviar no máximo {MAX_PHOTOS} fotos. "
                   f"Este imóvel já possui {len(existing_photos)}."
        )

    saved_photos = []

    # Garante que a pasta uploads exista
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    for file in files:
        filename = f"{property_id}_{file.filename}"
        file_path = os.path.join(UPLOAD_DIR, filename)

        # Salvar arquivo fisicamente
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        # Montar URL pública
        url_photo = f"/uploads/{filename}"

        # Salvar referência no banco
        photo_db = await db.propertyphoto.create(
            data={
                "property_id": property_id,
                "url_photo": url_photo
            }
        )

        saved_photos.append(photo_db)

    return {
        "message": "Fotos enviadas com sucesso!",
        "saved": saved_photos
    }


@router.delete("/{photo_id}")
async def delete_photo(photo_id: int, db: Prisma = Depends(get_db)):

    photo = await db.propertyphoto.find_unique(
        where={"id": photo_id}
    )

    if not photo:
        raise HTTPException(status_code=404, detail="Foto não encontrada")

    # Remover arquivo físico se existir
    real_path = photo.url_photo.replace("/uploads/", "uploads/")
    if os.path.exists(real_path):
        os.remove(real_path)

    await db.propertyphoto.delete(
        where={"id": photo_id}
    )

    return {"message": "Foto removida com sucesso"}


# -------------------------------------------------------
# GET PHOTO
# -------------------------------------------------------
@router.get("/public/{filename}")
def get_property_photo(filename: str):
    file_path = os.path.join("uploads", filename)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(file_path)

