from fastapi import FastAPI
from app.routes import prontuario, teleconsulta, internacao

from app.routes.administrativa import administrativa
from app.routes.consultas import consulta
from app.routes.exames import exame
from app.routes.historicos import historico
from app.routes.notificacoes import notificacao
from app.routes.pacientes import paciente
from app.routes.profissionais import profissional
from app.routes.receitas import receita

app = FastAPI(title="API Clínica Completa")

app.include_router(administrativa.router)
app.include_router(consulta.router)
app.include_router(exame.router)
app.include_router(historico.router)
app.include_router(paciente.router)
app.include_router(profissional.router)
app.include_router(receita.router)
app.include_router(notificacao.router)

app.include_router(prontuario.router)
app.include_router(teleconsulta.router)
app.include_router(internacao.router)

@app.get("/")
def root():
    return {"msg": "API da Clínica Médica Completa"}