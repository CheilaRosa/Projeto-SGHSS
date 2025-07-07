import sqlite3

DB_NAME = "clinica.db"

def criar_tabela_internacao():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        # Internações
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS internacoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_paciente INTEGER NOT NULL,
                id_profissional INTEGER NOT NULL,
                data_entrada TEXT NOT NULL,
                motivo TEXT NOT NULL,
                status TEXT NOT NULL,
                data_alta TEXT,
                FOREIGN KEY(id_paciente) REFERENCES pacientes(id)
            )
        ''')
        conn.commit()

def registrar_internacao(data):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO internacoes (id_paciente, id_profissional, data_entrada, motivo, status)
            VALUES (?, ?, ?, ?, ?)
        ''', (data["id_paciente"], data["id_profissional"], data["data_entrada"], data["motivo"], 'ativo'))
        conn.commit()
        return cursor.lastrowid

def registrar_alta(id_internacao, data_alta):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE internacoes
            SET status = 'alta', data_alta = ?
            WHERE id = ?
        ''', (data_alta, id_internacao))
        conn.commit()

def listar_internacoes(status=None):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        if status:
            cursor.execute('SELECT * FROM internacoes WHERE status = ?', (status,))
        else:
            cursor.execute('SELECT * FROM internacoes')
        return cursor.fetchall()

def buscar_internacao(id_internacao):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM internacoes WHERE id = ?', (id_internacao,))
        return cursor.fetchone()
    