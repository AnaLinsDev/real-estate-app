from fastapi import FastAPI
from app.routes import users, auth, properties, tenants, occupations

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["Users"])

app.include_router(properties.router, prefix="/properties", tags=["Properties"])
app.include_router(tenants.router, prefix="/tenants", tags=["Tenants"])

app.include_router(occupations.router, prefix="/occupations", tags=["Occupations"])

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
