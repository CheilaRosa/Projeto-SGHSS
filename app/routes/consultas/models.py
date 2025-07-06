import sqlite3

DB_NAME = "clinica.db"

def criar_tabelas_consulta():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        # Consultas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS consultas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_paciente INTEGER NOT NULL,
                id_profissional INTEGER NOT NULL,
                data TEXT NOT NULL,
                especialidade TEXT NOT NULL,
                status INTEGER DEFAULT (0),
                FOREIGN KEY(id_paciente) REFERENCES pacientes(id),
                FOREIGN KEY(id_profissional) REFERENCES profissionais_saude(id)
            )
        ''')
        conn.commit()

# Funções para histórico clínico:
def adicionar_consulta(data):

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO consultas (id_paciente, id_profissional, data, especialidade)
            VALUES (?, ?, ?, ?)
        ''', (data["id_paciente"], data["id_profissional"], data["data"], data["especialidade"]))
        conn.commit()

def alterar_status_consulta(id_consulta, status):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE consultas
            SET status = ?
            WHERE id = ?
        ''', (status, id_consulta))
        conn.commit()
        return cursor.rowcount
