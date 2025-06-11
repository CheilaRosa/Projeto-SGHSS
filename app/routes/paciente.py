from fastapi import APIRouter

router = APIRouter(prefix="/pacientes", tags=["Pacientes"])

@router.get("/")
def listar_pacientes():
    return [{"id": 1, "nome": "João"}, {"id": 2, "nome": "Maria"}]