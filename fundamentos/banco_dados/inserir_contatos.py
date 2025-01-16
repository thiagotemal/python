from bd import nova_conexao
from mysql.connector.errors import ProgrammingError

comando_inserir = "INSERT INTO contatos (nome, tel) VALUES (%s, %s)"
args = ('joaquim','1199555555')

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(comando_inserir,args)
        conexao.commit()
    except ProgrammingError as e:
        print(f"Erro ao inserir {e.msg}")
    else:
        print(f'contato inserido com id {cursor.lastrowid}')
