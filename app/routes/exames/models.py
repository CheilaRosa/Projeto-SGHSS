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
                resultado TEXT,
                FOREIGN KEY(id_paciente) REFERENCES pacientes(id),
                FOREIGN KEY(id_profissional) REFERENCES profissionais_saude(id)
            )
        ''')
        conn.commit()
        
def adicionar_exame(data):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO exames (id_paciente, id_profissional, nome, data)
            VALUES (?, ?, ?, ?)
        ''', (data["id_paciente"], data["id_profissional"], data["nome"], data["data"]))
        conn.commit()

def atualiza_resultado_exame(id: int, data):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE exames
            SET resultado = ?
            WHERE id = ?
        ''', (data["resultado"], id))
        conn.commit()
        return cursor.rowcount

def excluir_exame(id: int):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM exames WHERE id = ?', (id,))
        conn.commit()

def listar_exame(id_paciente):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT nome, data, resultado FROM exames WHERE id_paciente = ?', (id_paciente,))
        conn.commit()
        exames = cursor.fetchall()
        return {
            "exames": [{"nome": e[0], "data": e[1], "resultado": e[2]} for e in exames],
        }
