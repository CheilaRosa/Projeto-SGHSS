from fastapi import APIRouter
router = APIRouter(prefix="/prontuarios", tags=["Prontuários"])

@router.get("/")
def listar_prontuarios():
    return [{"paciente_id": 1, "historico": "Alergia a penicilina"}]