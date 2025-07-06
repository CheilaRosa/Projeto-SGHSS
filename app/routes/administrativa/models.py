import sqlite3
import hashlib
from app.routes.administrativa import auth


DB_NAME = "clinica.db"

def criar_tabela_administradora():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS administrativa (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL,
                senha TEXT NOT NULL,
                telefone TEXT,
                email TEXT,
                token TEXT
            )
        ''')
        conn.commit()

def cadastrar_administrator(dados):
    # Codifica a senha para bytes, pois o hashlib trabalha com bytes
    senha_bytes = dados['senha'].encode('utf-8')
    # Cria um objeto hash SHA-256
    senha_hash_object = hashlib.sha256(senha_bytes).hexdigest()

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO administrativa (usuario, senha, telefone, email, token)
            VALUES (?, ?, ?, ?, ?)
        ''', (dados['usuario'], senha_hash_object, dados['telefone'], dados['email'], None))
        conn.commit()
        return cursor.lastrowid
        
def excluir_administrator(id_administrator):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM administrativa WHERE id = ?', (id_administrator))
        conn.commit()
        return cursor.lastrowid

def faz_login(dados):    
    # Codifica a senha para bytes, pois o hashlib trabalha com bytes
    senha_bytes = dados['senha'].encode('utf-8')
    # Cria um objeto hash SHA-256
    senha_hash_object = hashlib.sha256(senha_bytes).hexdigest()

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM administrativa WHERE usuario = ? and senha = ?', (dados['usuario'], senha_hash_object))
        row = cursor.fetchone()
        if row:
            return {
                "id": row[0],
                "usuario": row[1]
            }
        return None

def guarda_token(dados):            
    id_usuario = dados["id"]
    save_token = auth.gerar_token_simples(dados["usuario"])
    
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE administrativa
            SET token = ?
            WHERE id = ?
        ''', (save_token, id_usuario))
        conn.commit()

    return {
        "status": "sucesso",
        "token": save_token
    }

def busca_token(token: str):                
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM administrativa WHERE token = ?', (token,))
        row = cursor.fetchone()
        if row:
            return True
        return False
