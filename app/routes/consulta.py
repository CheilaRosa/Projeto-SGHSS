from fastapi import APIRouter
router = APIRouter(prefix="/consultas", tags=["Consultas"])

@router.get("/")
def listar_consultas():
    return [{"id": 1, "paciente": "João", "data": "2025-06-10"}]