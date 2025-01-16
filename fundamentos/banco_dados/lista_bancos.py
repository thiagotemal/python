from mysql.connector import connect

conexao = connect(
    host= 'localhost',
    port= '3306',
    user='root',
    passwd='my-secret-pw'
)

cursor = conexao.cursor()
cursor.execute('SHOW DATABASES')

for i, databases in enumerate(cursor, start=1):
    print(f'BAnco de dados {i} {databases[0]}')
