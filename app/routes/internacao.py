from fastapi import APIRouter
router = APIRouter(prefix="/internacoes", tags=["Internações"])

@router.get("/")
def listar_internacoes():
    return [{"id": 1, "paciente": "João", "status": "em andamento"}]