from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.routes.notificacoes import models

router = APIRouter()

models.criar_tabelas_notificacao()

class NotificacaoPaciente(BaseModel):
    id_consulta: int

@router.post("/consulta/noficicacao")
def notificar_paciente_consulta(notificacao_paciente: NotificacaoPaciente):
    paciente_consulta = models.notificar_paciente_consulta(notificacao_paciente.dict())
    return paciente_consulta

@router.post("/exames/noficicacao")
def notificar_paciente_exame(notificacao_paciente: NotificacaoPaciente):
    paciente_exame = models.notificar_paciente_exame(notificacao_paciente.dict())
    return paciente_exame
