import sqlite3

DB_NAME = "clinica.db"

def criar_tabela_prontuarios():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS prontuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_internacao INTEGER NOT NULL,
                data_registro TEXT NOT NULL,
                descricao TEXT NOT NULL,
                tipo TEXT NOT NULL,
                FOREIGN KEY (id_internacao) REFERENCES internacoes(id)
            )
        ''')
        conn.commit()

def cadastrar_prontuario(data):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO prontuarios (id_internacao, data_registro, descricao, tipo)
            VALUES (?, ?, ?, ?)
        ''', (data["id_internacao"], data["data_registro"], data["descricao"], data["tipo"]))
        conn.commit()
        return cursor.lastrowid

def listar_prontuarios(id_internacao):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM prontuarios WHERE id_internacao = ?', (id_internacao,))
        return cursor.fetchall()

def atualizar_prontuario(id_prontuario, data):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE prontuarios
            SET descricao = ?, tipo = ?, data_registro = ?
            WHERE id = ?
        ''', (data["descricao"], data["tipo"], data["data_registro"], id_prontuario))
        conn.commit()
        return cursor.rowcount  # Quantidade de registros atualizados
    