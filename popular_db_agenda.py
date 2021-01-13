from random import choice, randint
from datetime import datetime
import sqlite3
import os

nomes = [
    'Ana', 'Alberto', 'Alfredo', 'Brenda', 'Breno', 'Bruno', 'Cassio',
    'Camila', 'Cleiton', 'Carla', 'Duda', 'Diego', 'Emerson', 'Evelyn',
    'Emilia', 'Fernanda', 'Francisco', 'Julia', 'Jose', 'Katy', 'Mateus',
    'Mariana', 'Paula', 'Pedro', 'Thiago', 'Tamires', 'Rosa', 'Renan'
]

sobrenomes = [
    'Abreu', 'Almeida', 'Alvares', 'Alencar', 'Bandeira', 'Borges', 'Braga',
    'Bueno', 'Bispo', 'Cavalcante', 'Cerqueira', 'Cruz', 'Dantas', 'Duarte',
    'Esteves', 'Espinola', 'Franco', 'Fontes', 'Garcia', 'Gomes', 'Lima',
    'Moreira', 'Maltes', 'Neto', 'Pereira', 'Pinheiro', 'Ribeiro'
]

lista_ddd = ['68', '82', '91', '96', '71', '75', '11', '28', '31', '14', '79']

caminho = os.path.dirname(os.path.realpath(__file__))
conexao = sqlite3.connect(os.path.join(caminho, 'db.sqlite3'))

cursor = conexao.cursor()

for i in range(100):
    nome = choice(nomes)
    sobrenome = choice(sobrenomes) 
    numero = f'{choice(lista_ddd)} 9{randint(1000, 9999)} {randint(1000, 9999)}'
    email = f'{nome}{randint(1, 100)}@email.com'
    categoria = randint(1, 4)
    data_criacao = data_criacao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sql = 'INSERT INTO contatos_contato'\
            '(nome, sobrenome, telefone, email, descricao, categoria_id, data_criacao)'\
            f'VALUES ("{nome}", "{sobrenome}", "{numero}", "{email}",'\
            f'"Lorem ipsum", "{categoria}", "{data_criacao}");'
    
    cursor.execute(sql)

conexao.commit()
conexao.close()
