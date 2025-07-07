from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.routes.teleconsulta import models
from app.routes.administrativa import auth

router = APIRouter()
models.criar_tabela_prontuarios_teleconsulta()

class ProntuarioTeleconsulta(BaseModel):
    id_paciente: int
    id_profissional: int
    data_consulta: str
    descricao: str
    diagnostico: str = None
    conduta: str = None
    link_teleconsulta: str = None


@router.post("/teleconsulta/{id_teleconsulta}")
def agendar_teleconsulta(id_teleconsulta: int):
    url = models.gerar_link_sala_teleconsulta()
    models.atualizar_prontuario_teleconsulta(id_teleconsulta, url)
    return {"sala_teleconsulta": url}

@router.post("/teleconsulta/prontuarios/")
def criar_prontuario_teleconsulta(prontuario: ProntuarioTeleconsulta):
    id_prontuario = models.cadastrar_prontuario_teleconsulta(prontuario.dict())
    return {"id_prontuario": id_prontuario}

@router.get("/teleconsulta/prontuarios/{id_paciente}")
def listar_prontuarios_teleconsulta(id_paciente: int):
    registros = models.listar_prontuarios_teleconsulta(id_paciente)
    return {"prontuarios": registros}
