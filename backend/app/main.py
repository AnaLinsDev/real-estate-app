from fastapi import FastAPI
from app.routes import users, auth, properties

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(properties.router, prefix="/properties", tags=["Properties"])

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
