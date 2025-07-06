from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.routes.pacientes import models
from app.routes.administrativa import auth

router = APIRouter()

models.criar_tabela_paciente()

class Pacientes(BaseModel):
    nome: str
    cpf: str
    telefone: str
    email: str

@router.post("/pacientes/{token}/")
def criar_paciente(token:str, JsonPaciente: Pacientes):
    if auth.valida_token(token):
        try:
            paciente_id = models.cadastrar_paciente(JsonPaciente.dict())
            return {"mensagem": "Paciente cadastrado com sucesso", "id": paciente_id}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
    else:
        raise HTTPException(status_code=404, detail="Sem autorização")

@router.put("/pacientes/{token}/{id_paciente}")
def atualizar_paciente(token:str, id_paciente: int, JsonPaciente: Pacientes):
    if auth.valida_token(token):
        linhas_afetadas = models.editar_paciente(id_paciente, JsonPaciente.dict())
        if linhas_afetadas == 0:
            raise HTTPException(status_code=404, detail="Paciente não encontrado")
        return {"mensagem": "Cadastro atualizado com sucesso"}
    else:
        raise HTTPException(status_code=404, detail="Sem autorização")

@router.get("/pacientes/{var_paciente}")
def obter_paciente(var_paciente: str):
    if var_paciente.isdigit():
        id_paciente = int(var_paciente)
        JsonPaciente = models.consultar_paciente(id_paciente)
        if not JsonPaciente:
            raise HTTPException(status_code=404, detail="Paciente não encontrado")
    else:
        JsonPaciente = models.buscar_pacientes_por_nome(var_paciente)
        if not JsonPaciente:
            raise HTTPException(status_code=404, detail="Paciente não encontrado")
    return JsonPaciente