from fastapi import FastAPI
from app.routes import users, auth, properties, tenants, occupations, property_bills, property_investments, property_photos
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

# ONLY IN DEVELOPMENT
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,     
    allow_credentials=True,
    allow_methods=["*"],         
    allow_headers=["*"],        
)

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

app.include_router(users.router, prefix="/users", tags=["Users"])

app.include_router(properties.router, prefix="/properties", tags=["Properties"])
app.include_router(tenants.router, prefix="/tenants", tags=["Tenants"])

app.include_router(occupations.router, prefix="/occupations", tags=["Occupations"])
app.include_router(property_bills.router, prefix="/property-bills", tags=["Property Bills"])
app.include_router(property_investments.router, prefix="/property-investments", tags=["Property Investments"])
app.include_router(property_photos.router, prefix="/property-photos", tags=["Property Photos"])

app.include_router(auth.router, prefix="/auth", tags=["Auth"])

