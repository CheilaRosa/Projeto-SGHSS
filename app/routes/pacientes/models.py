import sqlite3

DB_NAME = "clinica.db"

def criar_tabela_paciente():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pacientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf TEXT UNIQUE NOT NULL,
                telefone TEXT,
                email TEXT
            )
        ''')
        conn.commit()

def cadastrar_paciente(dados):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO pacientes (nome, cpf, telefone, email)
            VALUES (?, ?, ?, ?)
        ''', (dados['nome'], dados['cpf'], dados['telefone'], dados['email']))
        conn.commit()
        return cursor.lastrowid

def editar_paciente(id_paciente, dados):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE pacientes
            SET nome = ?, cpf = ?, telefone = ?, email = ?
            WHERE id = ?
        ''', (dados['nome'], dados['cpf'], dados['telefone'], dados['email'], id_paciente))
        conn.commit()
        return cursor.rowcount

def consultar_paciente(id_paciente):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM pacientes WHERE id = ?', (id_paciente,))
        row = cursor.fetchone()
        if row:
            return {
                "id": row[0],
                "nome": row[1],
                "cpf": row[2],
                "telefone": row[3],
                "email": row[4]
            }
        return None
    
def buscar_pacientes_por_nome(parte_nome):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM pacientes
            WHERE nome LIKE ?
        ''', (f'%{parte_nome}%',))
        rows = cursor.fetchall()
        pacientes = []
        for row in rows:
            pacientes.append({
                "id": row[0],
                "nome": row[1],
                "cpf": row[2],
                "telefone": row[3],
                "email": row[4]
            })
        return pacientes
