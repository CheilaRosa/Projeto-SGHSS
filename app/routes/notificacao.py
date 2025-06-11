from fastapi import APIRouter
router = APIRouter(prefix="/notificacoes", tags=["Notificações"])

@router.get("/")
def listar_notificacoes():
    return [{"id": 1, "mensagem": "Consulta marcada para amanhã"}]