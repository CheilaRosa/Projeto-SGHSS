import sqlite3

DB_NAME = "clinica.db"

def criar_tabela_profissionais():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS profissionais_saude (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                profissao TEXT NOT NULL,
                registro TEXT UNIQUE NOT NULL,
                telefone TEXT,
                email TEXT
            )
        ''')
        conn.commit()

def cadastrar_profissional(dados):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO profissionais_saude (nome, profissao, registro, telefone, email)
            VALUES (?, ?, ?, ?, ?)
        ''', (dados['nome'], dados['profissao'], dados['registro'], dados['telefone'], dados['email']))
        conn.commit()
        return cursor.lastrowid

def editar_profissional(id_profissional, dados):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE profissionais_saude
            SET nome = ?, profissao = ?, registro = ?, telefone = ?, email = ?
            WHERE id = ?
        ''', (dados['nome'], dados['profissao'], dados['registro'], dados['telefone'], dados['email'], id_profissional))
        conn.commit()
        return cursor.rowcount

def buscar_profissionais_por_nome(parte_nome):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM profissionais_saude
            WHERE nome LIKE ?
        ''', (f'%{parte_nome}%',))
        rows = cursor.fetchall()
        profissionais = []
        for row in rows:
            profissionais.append({
                "id": row[0],
                "nome": row[1],
                "profissao": row[2],
                "registro": row[3],
                "telefone": row[4],
                "email": row[5]
            })
        return profissionais
