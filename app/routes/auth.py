from fastapi import APIRouter
router = APIRouter(prefix="/auth", tags=["Autenticação"])

@router.post("/login")
def login():
    return {"access_token": "fake-jwt-token"}