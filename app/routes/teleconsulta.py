from fastapi import APIRouter
router = APIRouter(prefix="/teleconsulta", tags=["Telemedicina"])

@router.get("/")
def listar_sessoes():
    return [{"id": 1, "paciente": "João", "profissional": "Dr. Ana"}]