from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.routes.exames import models

router = APIRouter()
models.criar_tabelas_exame()

class Exame(BaseModel):
    paciente: int
    nome: str
    data: str

@router.post("/exame/{id_profissional}/")
def adicionar_exame(id_profissional: int, exame: Exame):
    try:
        models.adicionar_exame(id_profissional, exame.paciente, exame.nome, exame.data)
        return {"mensagem": "Exame adicionado com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    