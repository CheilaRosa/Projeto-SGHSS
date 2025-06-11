from fastapi import APIRouter
router = APIRouter(prefix="/profissionais", tags=["Profissionais"])

@router.get("/")
def listar_profissionais():
    return [{"id": 1, "nome": "Dr. Ana"}]