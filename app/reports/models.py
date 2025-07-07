import sqlite3

DB_NAME = "clinica.db"

def relatorio_administrativo(periodo_inicio, periodo_fim):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        
        # Total de internações no período
        cursor.execute('''
            SELECT COUNT(*) FROM internacoes
            WHERE data_entrada BETWEEN ? AND ?
        ''', (periodo_inicio, periodo_fim))
        total_internacoes = cursor.fetchone()[0]
        
        # Total de teleconsultas no período
        cursor.execute('''
            SELECT COUNT(*) FROM prontuarios_teleconsulta
            WHERE data_consulta BETWEEN ? AND ?
        ''', (periodo_inicio, periodo_fim))
        total_teleconsultas = cursor.fetchone()[0]
        
        return {
            "total_internacoes": total_internacoes,
            "total_teleconsultas": total_teleconsultas,
        }

def relatorio_clinico_paciente(id_paciente):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        
        # Internações
        cursor.execute('SELECT * FROM internacoes WHERE id_paciente = ?', (id_paciente,))
        internacoes = cursor.fetchall()
        
        # Prontuários Teleconsulta
        cursor.execute('SELECT * FROM prontuarios_teleconsulta WHERE id_paciente = ?', (id_paciente,))
        teleconsultas = cursor.fetchall()
        
        return {
            "internacoes": internacoes,
            "teleconsultas": teleconsultas
        }