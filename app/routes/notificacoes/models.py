import sqlite3

DB_NAME = "clinica.db"

def criar_tabelas_notificacao():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        # Consultas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS notificacoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_paciente INTEGER NOT NULL,
                id_profissional INTEGER NOT NULL,
                mensagem TEXT NOT NULL,
                FOREIGN KEY(id_paciente) REFERENCES pacientes(id),
                FOREIGN KEY(id_profissional) REFERENCES profissionais_saude(id)
            )
        ''')
        conn.commit()

# Funções para histórico clínico:
def notificar_paciente_consulta(data):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''SELECT id_paciente, id_profissional, data, especialidade 
                       FROM consultas WHERE id = ?''', (data["id_consulta"],))
        row = cursor.fetchone()
        if row:
            id_paciente = row[0]
            id_profissional = row[1]
            data_mensagem = row[2]
            especialidade = row[3]
     
    with sqlite3.connect(DB_NAME) as conn:   
        cursor = conn.cursor()
        cursor.execute('SELECT nome FROM pacientes WHERE id = ?', (id_paciente,))
        row = cursor.fetchone()
        if row:
            nome_paciente = row[0]
    
    with sqlite3.connect(DB_NAME) as conn:    
        cursor = conn.cursor()
        cursor.execute('SELECT nome FROM profissionais_saude WHERE id = ?', (id_profissional,))
        row = cursor.fetchone()
        if row:
            nome_profissional = row[0]

    mensagem = 'Prezado '+nome_paciente+' sua consulta com o doutor(a) '+nome_profissional+', na especialidade '+especialidade+', será no dia: '+data_mensagem

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO notificacoes (id_paciente, id_profissional, mensagem)
            VALUES (?, ?, ?)
        ''', (id_paciente, id_profissional, mensagem, ))
        conn.commit()
        return {
            "id": cursor.lastrowid,
            "mensagem": mensagem 
        }

def notificar_paciente_exame(data):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''SELECT id_paciente, id_profissional, nome, data, resultado 
                       FROM exames WHERE id = ?''', (data["id_consulta"],))
        row = cursor.fetchone()
        if row:
            id_paciente = row[0]
            id_profissional = row[1]
            nome_exame = row[2]
            data_mensagem = row[3]
            resultado = row[4]
     
    with sqlite3.connect(DB_NAME) as conn:   
        cursor = conn.cursor()
        cursor.execute('SELECT nome FROM pacientes WHERE id = ?', (id_paciente,))
        row = cursor.fetchone()
        if row:
            nome_paciente = row[0]
    
    with sqlite3.connect(DB_NAME) as conn:    
        cursor = conn.cursor()
        cursor.execute('SELECT nome FROM profissionais_saude WHERE id = ?', (id_profissional,))
        row = cursor.fetchone()
        if row:
            nome_profissional = row[0]

    mensagem = 'Prezado '+nome_paciente+' seu exame solicitado pelo(a) doutor(a) '+nome_profissional+', de '+nome_exame+', será no dia: '+data_mensagem

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO notificacoes (id_paciente, id_profissional, mensagem)
            VALUES (?, ?, ?)
        ''', (id_paciente, id_profissional, mensagem, ))
        conn.commit()
        return {
            "id": cursor.lastrowid,
            "mensagem": mensagem 
        }
