## Real State App

python -m venv venv
venv\Scripts\activate

prisma migrate dev --name init
prisma generate

uvicorn app.main:app --reload
_______

