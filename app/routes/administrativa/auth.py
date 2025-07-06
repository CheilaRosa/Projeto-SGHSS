import hashlib
import time

SEGREDO = "22c87f22abf5379fda2613792766b9d4"

def gerar_token_simples(dados: str):
    timestamp = str(int(time.time()))
    usuario_bytes = dados.encode('utf-8')
    usuario_hash_object = hashlib.sha256(usuario_bytes).hexdigest()
    bruto = usuario_hash_object + timestamp + SEGREDO
    token_bytes = bruto.encode('utf-8')
    token = hashlib.sha256(token_bytes).hexdigest()
    return token

