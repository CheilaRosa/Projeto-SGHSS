from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.routes.receitas import models

router = APIRouter()
models.criar_tabelas_receita()

class Receita(BaseModel):
    paciente: int
    descricao: str
    data: str

@router.post("/receita/{id_profissional}")
def adicionar_receita(id_profissional: int, receita: Receita):
    models.adicionar_receita(id_profissional, receita.paciente, receita.descricao, receita.data)
    return {"mensagem": "Receita adicionada com sucesso"}