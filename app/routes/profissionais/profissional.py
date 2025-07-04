from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.routes.profissionais import models
router = APIRouter()

models.criar_tabela_profissionais()

class ProfissionalSaude(BaseModel):
    nome: str
    profissao: str
    registro: str
    telefone: str
    email: str

@router.post("/profissional/")
def criar_profissional(json_profissional: ProfissionalSaude):
    try:
        profissional_id = models.cadastrar_profissional(json_profissional.dict())
        return {"mensagem": "Profissional cadastrado com sucesso", "id": profissional_id}    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/profissional/")
def buscar_profissionais(nome: str):
    json_profissional = models.buscar_profissionais_por_nome(nome)
    if not json_profissional:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    return json_profissional