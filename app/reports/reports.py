from fastapi import APIRouter, Query, HTTPException
from app.reports import models
from app.routes.administrativa import auth

router = APIRouter()

#Exemplo = /relatorios/{token}/administrativo?periodo_inicio=2025-07-01&periodo_fim=2025-07-31
@router.get("/relatorios/{token}/administrativo")
def gerar_relatorio_administrativo(token: str, periodo_inicio: str = Query(...), periodo_fim: str = Query(...)):
    if auth.valida_token(token):
        relatorio = models.relatorio_administrativo(periodo_inicio, periodo_fim)
        return relatorio
    else:
        raise HTTPException(status_code=404, detail="Sem autorização")

@router.get("/relatorios/{token}/clinico/{id_paciente}")
def gerar_relatorio_clinico(token: str, id_paciente: int):
    if auth.valida_token(token):
        relatorio = models.relatorio_clinico_paciente(id_paciente)
        return relatorio
    else:
        raise HTTPException(status_code=404, detail="Sem autorização")