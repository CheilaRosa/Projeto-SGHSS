import hashlib
import time
from app.routes.administrativa import models

__SEGREDO = "22c87f22abf"

def gerar_token_simples(dados: str) -> str:
    timestamp = str(int(time.time()))
    bruto = dados + timestamp + __SEGREDO
    token_bytes = bruto.encode('utf-8')
    token = hashlib.sha256(token_bytes).hexdigest()
    #token_32 = token[:32]  # Pega apenas os 32 primeiros caracteres
    return token
    #token_32

def valida_token(token: str):
    return models.busca_token(token)