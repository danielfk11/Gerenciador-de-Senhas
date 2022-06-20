import sqlite3

senha_admin = 'admin123' # ALTERAVEL

senha = input("Insira a senha do admin: ")
if senha != senha_admin:
    print("Senha incorreta tente novamente...")
    senha = input("Insira a senha do admin: ")
    if senha != senha_admin:
        print("Senha incorreta tente novamente...")
        senha = input("Insira a senha do admin: ")
        if senha != senha_admin:
            print("Senha incorreta muitas vezes... saindo..")
            exit()


connect = sqlite3.connect("senhas.db")

cursor = connect.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    service TEXT NO NULL
);
''')

def menu():
    print('-----------------------------------------')
    print(' *1* para inserir uma nova senha')
    print(' *2* listar os services salvos')
    print(' *3* para recuperar sua senha')
    print(' *0* para fechar o menu')
    print('-----------------------------------------')


def peg_senha(service):
    pass

def mostrar_senha(service):
    cursor.execute(f'''
        SELECT username, password FROM users
        WHERE service = '{service}'
    ''')

    if cursor.rowcount == 0:
        print("Servico nao encotrado, verifique o nome digitado.")
    else:
        for user in cursor.fetchall():
            print(user)

def nova_senha(service, username, password):
    cursor.execute(f'''
        INSERT INTO users (service, username, password) 
        VALUES ('{service}', '{username}', '{password}')
    ''')
    connect.commit()

def mostrar_servicos():
    cursor.execute('''
        SELECT service FROM users;
    ''')
    for service in cursor.fetchall():
        print(service)

while True:
    menu()
    selecionar = input("Selecione um numero para continuar: ")
    if selecionar not in ['1', '2', '3', '0']:
        print("Selecione apenas numeros validos.")
        continue

    if selecionar == '0':
        print('Saindo do sistema....')
        break

    if selecionar == '1':
        service = input("Qual o nome do servico? ")
        username = input("Qual o nome de usuario? ")
        password = input("Qual a senha? ")
        nova_senha(service, username, password)

    if selecionar == '2':
        mostrar_servicos()

    if selecionar == '3':
        service = input("Qual servico voce deseja ver a senha? ")
        mostrar_senha(service)

connect.close()