from fastapi import FastAPI
from app.routes import paciente, profissional, consulta, auth, prontuario, receita, teleconsulta, notificacao, internacao
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Clínica Completa")

app.include_router(paciente.router)
app.include_router(profissional.router)
app.include_router(consulta.router)
app.include_router(auth.router)
app.include_router(prontuario.router)
app.include_router(receita.router)
app.include_router(teleconsulta.router)
app.include_router(notificacao.router)
app.include_router(internacao.router)

@app.get("/")
def root():
    return {"msg": "API da Clínica Médica Completa"}