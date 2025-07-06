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

@router.delete("/receita/{id_receita}")
def excluir_exame(id_receita: int):
    try:
        models.excluir_receita(id_receita)
        return {"mensagem": "Exame excluido com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/receita/{id_paciente}")
def listar_exame(id_paciente: int):
    try:
        json_receitas = models.listar_receita(id_paciente)
        return json_receitas
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
