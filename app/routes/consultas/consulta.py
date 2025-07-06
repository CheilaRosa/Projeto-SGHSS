from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.routes.consultas import models
from app.routes.administrativa import auth
router = APIRouter()

models.criar_tabelas_consulta()

class Consulta(BaseModel):
    id_paciente: int
    id_profissional: int
    data: str
    especialidade: str

'''
Status é representado por:
0 -> Marcado
1 -> Atendido
2 -> Internado
3 -> Cancelado
'''

@router.post("/consulta/{token}/")
def adicionar_consulta(token:str, consulta: Consulta):
    if auth.valida_token(token):
        try:
            models.adicionar_consulta(consulta.dict())
            return {"mensagem": "Consulta adicionada com sucesso"}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
    else:
        raise HTTPException(status_code=404, detail="Sem autorização")
    

@router.put("/consulta/{id_consulta}/{status}")
def alterar_status_consulta(id_consulta:int, status: int):
    try:
        models.alterar_status_consulta(id_consulta, status)
        return {"mensagem": "Atlterado status com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/consulta/{id_paciente}")
def listar_exame(id_paciente: int):
    try:
        json_consultas = models.listar_consulta(id_paciente)
        return json_consultas
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
