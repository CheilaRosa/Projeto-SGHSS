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
                FOREIGN KEY(id_paciente) REFERENCES pacientes(id),
                FOREIGN KEY(id_profissional) REFERENCES profissionais_saude(id)
            )
        ''')
        conn.commit()

# Funções para histórico clínico:
def adicionar_consulta(id_paciente, data, especialidade):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO consultas (id_paciente, data, especialidade)
            VALUES (?, ?, ?)
        ''', (id_paciente, data, especialidade))
        conn.commit()