import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Rkot526.',
    database='bd_aula',

)
cursor = conexao.cursor()

# crud
# CREATE
nome_produto = "chocolate"
valor = 15
comando = f'INSERT INTO vendas (nome_produto,valor_produto) VALUES ("{nome_produto}",{valor})'
cursor.execute(comando)
conexao.commit()  # edita o banco de dados


cursor.close()
conexao.close()


"""
# CREATE
# nome_produto = "chocolate"
# valor = 15
# comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados


# READ
# comando = f'SELECT * FROM vendas'
# cursor.execute(comando)
# resultado = cursor.fetchall() # ler o banco de dados
# print(resultado)


# UPDATE
# nome_produto = "todynho"
# valor = 6
# comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados

# DELETE
# nome_produto = "todynho"
# comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados
"""
