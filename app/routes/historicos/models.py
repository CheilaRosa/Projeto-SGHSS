import sqlite3

DB_NAME = "clinica.db"

def obter_historico_clinico(id_paciente):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        # Consultas
        cursor.execute('''SELECT data, especialidade, (
                        CASE 
                            WHEN status = 0 THEN 'MARCADO'
                            WHEN status = 1 THEN 'ATENDIDO'
                            WHEN status = 2 THEN 'INTERNADO'
                            ELSE 'CANCELADO'
                        END
                        ) FROM consultas WHERE id_paciente = ?''', (id_paciente,))
        consultas = cursor.fetchall()

        # Exames
        cursor.execute('SELECT nome, data, resultado FROM exames WHERE id_paciente = ?', (id_paciente,))
        exames = cursor.fetchall()

        # Receitas
        cursor.execute('SELECT descricao, data FROM receitas WHERE id_paciente = ?', (id_paciente,))
        receitas = cursor.fetchall()

        return {
            "consultas": [{"data": c[0], "especialidade": c[1], "status": c[2]} for c in consultas],
            "exames": [{"nome": e[0], "data": e[1], "resultado": e[2]} for e in exames],
            "receitas": [{"descricao": r[0], "data": r[1]} for r in receitas],
        }