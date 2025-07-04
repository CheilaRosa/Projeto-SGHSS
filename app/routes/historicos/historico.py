from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.routes.historicos import models

router = APIRouter()

# Histórico Clínico:
@router.get("/historico/{id_paciente}")
def obter_historico(id_paciente: int):
    historico = models.obter_historico_clinico(id_paciente)
    return historico