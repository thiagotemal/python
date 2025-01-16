from bd import nova_conexao
from mysql.connector.errors import ProgrammingError



consulta = "select * from contatos"

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(consulta)
        contatos = cursor.fetchall()
    except ProgrammingError as e:
        print(f"erro ao consultar {e.msg}")
    else:
        for contato in contatos:
            print(f'contato {contato[0]} - {contato[1]}')
