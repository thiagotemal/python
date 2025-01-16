from mysql.connector import connect
conexao = connect(host='localhost',
                  port=3306,
                  passwd='my-secret-pw',
                  user='root'

)

cursor = conexao.cursor()
cursor.execute('CREATE DATABASE agenda')