from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.routes.prontuarios import models
from app.routes.administrativa import auth

router = APIRouter()
models.criar_tabela_prontuarios()

class Prontuario(BaseModel):
    id_internacao: int
    data_registro: str
    descricao: str
    tipo: str

@router.post("/prontuarios/{token}")
def criar_prontuario(token: str, prontuario: Prontuario):
    if auth.valida_token(token):
        id_prontuario = models.cadastrar_prontuario(prontuario.dict())
        return {"id_prontuario": id_prontuario}
    else:
        raise HTTPException(status_code=404, detail="Sem autorização")

@router.get("/prontuarios/{id_internacao}")
def listar_prontuarios(id_internacao: int):
    registros = models.listar_prontuarios(id_internacao)
    return {"prontuarios": registros}

@router.put("/prontuarios/{id_prontuario}")
def atualizar_prontuario(id_prontuario: int, prontuario: Prontuario):
    registros_afetados = models.atualizar_prontuario(id_prontuario, prontuario.dict())
    if registros_afetados == 0:
        raise HTTPException(status_code=404, detail="Registro não encontrado")
    return {"mensagem": "Registro do prontuário atualizado com sucesso"}