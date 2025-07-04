from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.routes.consultas import models
router = APIRouter()

models.criar_tabelas_consulta()

class Consulta(BaseModel):
    data: str
    especialidade: str

@router.post("/consulta/{id_paciente}")
def adicionar_consulta(id_paciente: int, consulta: Consulta):
    models.adicionar_consulta(id_paciente, consulta.data, consulta.especialidade)
    return {"mensagem": "Consulta adicionada com sucesso"}

#Alterar Ainda