import sqlite3
import secrets

DB_NAME = "clinica.db"

def criar_tabela_prontuarios_teleconsulta():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS prontuarios_teleconsulta (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_paciente INTEGER NOT NULL,
                id_profissional INTEGER NOT NULL,
                data_consulta TEXT NOT NULL,
                profissional TEXT NOT NULL,
                descricao TEXT NOT NULL,
                diagnostico TEXT,
                conduta TEXT,
                link_teleconsulta TEXT,
                FOREIGN KEY (id_paciente) REFERENCES pacientes(id),
                FOREIGN KEY (id_profissional) REFERENCES profissionais_saude(id)
            )
        ''')
        conn.commit()

def cadastrar_prontuario_teleconsulta(data):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO prontuarios_teleconsulta 
            (id_paciente, data_consulta, id_profissional, descricao, diagnostico, conduta, link_teleconsulta)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (data["id_paciente"], data["data_consulta"], data["id_profissional"], 
              data["descricao"], data["diagnostico"], data["conduta"], data["link_teleconsulta"]))
        conn.commit()
        return cursor.lastrowid

def listar_prontuarios_teleconsulta(id_paciente):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM prontuarios_teleconsulta WHERE id_paciente = ?', (id_paciente,))
        return cursor.fetchall()
    
def atualizar_prontuario_teleconsulta(id_prontuario, link_teleconsulta):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE prontuarios_teleconsulta SET link_teleconsulta = ? WHERE id = ?', (link_teleconsulta, id_prontuario))
        conn.commit()
        return cursor.rowcount

def gerar_link_sala_teleconsulta():
    nome_sala = "TeleConsulta_" + secrets.token_hex(8)
    url = f"https://meet.jit.si/{nome_sala}"
    return url