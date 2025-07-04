import sqlite3

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
        