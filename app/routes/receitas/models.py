import sqlite3
import hmac
import hashlib
import json

DB_NAME = "clinica.db"

def criar_tabelas_receita():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        # Receitas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS receitas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_paciente INTEGER NOT NULL,
                id_profissional INTEGER NOT NULL,
                descricao TEXT NOT NULL,
                data TEXT NOT NULL,
                FOREIGN KEY(id_paciente) REFERENCES pacientes(id),
                FOREIGN KEY(id_profissional) REFERENCES profissionais_saude(id)
            )
        ''')
        conn.commit()
        

def adicionar_receita(id_profisional,id_paciente, descricao, data):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO receitas (id_paciente, id_profissional, descricao, data)
            VALUES (?, ?, ?, ?)
        ''', (id_paciente, id_profisional, descricao, data))
        conn.commit()

def excluir_receita(id: int):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM receitas WHERE id = ?', (id,))
        conn.commit()

def listar_receita(id_paciente):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT descricao, data FROM receitas WHERE id_paciente = ?', (id_paciente,))
        conn.commit()
        receitas = cursor.fetchall()
        return {
            "receitas": [{"descricao": r[0], "data": r[1]} for r in receitas],
        }
        
def gerar_assinatura(id_profissional, receita):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT registro FROM profissionais_saude WHERE nome id ?
        ''', (id_profissional))
        rows = cursor.fetchall()
    receita_json = json.dumps(receita, sort_keys=True).encode()
    assinatura = hmac.new(rows[0], receita_json, hashlib.sha256).hexdigest()
    return assinatura
        