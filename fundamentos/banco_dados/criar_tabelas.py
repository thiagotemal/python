from bd import nova_conexao
from mysql.connector.errors import ProgrammingError


tabela_contatos = 'CREATE TABLE contatos(nome VARCHAR(50), tel VARCHAR(40))'
tabela_emails = 'CREATE TABLE emails(id INT AUTO_INCREMENT PRIMARY KEY, dono VARCHAR(50))'

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(tabela_contatos)
        cursor.execute(tabela_emails)
    except ProgrammingError as e:
        print(f"erro bd {e.msg}")
