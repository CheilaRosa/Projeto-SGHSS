from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.routes.internacoes import models
from app.routes.administrativa import auth

router = APIRouter()
models.criar_tabela_internacao()

class Internacao(BaseModel):
    id_paciente: int
    id_profissional: int
    data_entrada: str
    motivo: str

class Alta(BaseModel):
    data_alta: str

@router.post("/internacoes/{token}")
def internar_paciente(token: str, internacao: Internacao):
    if auth.valida_token(token):
        id_internacao = models.registrar_internacao(internacao.dict())
        return {"id_internacao": id_internacao}
    else:
        raise HTTPException(status_code=404, detail="Sem autorização")

@router.post("/internacoes/{id_internacao}/alta")
def dar_alta(id_internacao: int, alta: Alta):
    models.registrar_alta(id_internacao, alta.data_alta)
    return {"mensagem": "Alta registrada com sucesso"}

@router.get("/internacoes/")
def listar_todas_internacoes(status: str = None):
    internacoes = models.listar_internacoes(status)
    return {"internacoes": internacoes}

@router.get("/internacoes/{id_internacao}")
def detalhes_internacao(id_internacao: int):
    internacao = models.buscar_internacao(id_internacao)
    if not internacao:
        raise HTTPException(status_code=404, detail="Internação não encontrada")
    return {"internacao": internacao}