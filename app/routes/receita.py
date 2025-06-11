from fastapi import APIRouter
router = APIRouter(prefix="/receitas", tags=["Receitas"])

@router.get("/")
def listar_receitas():
    return [{"id": 1, "medicamento": "Dipirona"}]