from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.routes.exames import models

router = APIRouter()
models.criar_tabelas_exame()

class Exame(BaseModel):
    id_paciente: int
    id_profissional: int
    nome: str
    data: str

class Resultado(BaseModel):
    resultado: str

@router.post("/exame/")
def adicionar_exame(exame: Exame):
    try:
        models.adicionar_exame(exame.dict())
        return {"mensagem": "Exame adicionado com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/exame/resultado/{id_exame}")
def adicionar_exame(id_exame: int, resultado: Resultado):
    try:
        models.atualiza_resultado_exame(id_exame, resultado.dict())
        return {"mensagem": "Exame Atualizado com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.delete("/exame/{id_exame}")
def excluir_exame(id_exame: int):
    try:
        models.excluir_exame(id_exame)
        return {"mensagem": "Exame excluido com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/exame/{id_paciente}")
def listar_exame(id_paciente: int):
    try:
        json_exames = models.listar_exame(id_paciente)
        return json_exames
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    