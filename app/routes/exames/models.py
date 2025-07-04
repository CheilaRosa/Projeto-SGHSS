import sqlite3

DB_NAME = "clinica.db"

def criar_tabelas_exame():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()        
        # Exames
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS exames (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_paciente INTEGER NOT NULL,
                id_profissional INTEGER NOT NULL,
                nome TEXT NOT NULL,
                data TEXT NOT NULL,
                FOREIGN KEY(id_paciente) REFERENCES pacientes(id),
                FOREIGN KEY(id_profissional) REFERENCES profissionais_saude(id)
            )
        ''')
        conn.commit()
        
def adicionar_exame(id_profissional,id_paciente, nome, data):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO exames (id_paciente, id_profissional, nome, data)
            VALUES (?, ?, ?, ?)
        ''', (id_paciente, id_profissional, nome, data))
        conn.commit()