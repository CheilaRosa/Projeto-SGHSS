from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.routes.administrativa import models
router = APIRouter()

models.criar_tabela_administradora()

class Cad_Administradora(BaseModel):
    usuario: str
    senha: str
    telefone: str
    email: str

class Log_Administradora(BaseModel):
    usuario: str
    senha: str

@router.post("/administrator/cadastro/")
def criar_administrator(json_administrator: Cad_Administradora):
    try:
        id_administrator = models.cadastrar_administrator(json_administrator.dict())
        return {"mensagem": "Administrator cadastrado com sucesso", "id": id_administrator}    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete("/administrator/{id_administrator}")
def excluir_administrator(id_administrator: int):
    try:
        json_administrator = models.excluir_administrator(id_administrator)
        return {"mensagem": "Administrator excluido com sucesso", "id": json_administrator}    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/administrator/login/")
def buscar_administrator(json_administrator: Log_Administradora):
    json_login = models.faz_login(json_administrator.dict())
    if not json_login:
        raise HTTPException(status_code=404, detail="Administrator não encontrado")
    else:
        json_token = models.guarda_token(json_login)        
        if not json_token:
            raise HTTPException(status_code=404, detail="Administrator não encontrado")
    return json_token
