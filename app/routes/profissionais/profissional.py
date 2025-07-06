from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.routes.profissionais import models
from app.routes.administrativa import auth
router = APIRouter()

models.criar_tabela_profissionais()

class ProfissionalSaude(BaseModel):
    nome: str
    profissao: str
    registro: str
    telefone: str
    email: str

@router.post("/profissional/{token}/")
def criar_profissional(token:str, json_profissional: ProfissionalSaude):
    if auth.valida_token(token):
        try:
            profissional_id = models.cadastrar_profissional(json_profissional.dict())
            return {"mensagem": "Profissional cadastrado com sucesso", "id": profissional_id}    
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
    else:
        raise HTTPException(status_code=404, detail="Sem autorização")

@router.put("/profissional/{token}/{id_proficional}")
def atualizar_profissional(token:str, id_proficional: int, JsonPaciente: ProfissionalSaude):
    if auth.valida_token(token):
        linhas_afetadas = models.editar_profissional(id_proficional, JsonPaciente.dict())
        if linhas_afetadas == 0:
            raise HTTPException(status_code=404, detail="profissional não encontrado")
        return {"mensagem": "Cadastro atualizado com sucesso"}
    else:
        raise HTTPException(status_code=404, detail="Sem autorização")

@router.get("/profissional/{nome}")
def buscar_profissionais(nome: str):
    json_profissional = models.buscar_profissionais_por_nome(nome)
    if not json_profissional:
        raise HTTPException(status_code=404, detail="profissional não encontrado")
    return json_profissional