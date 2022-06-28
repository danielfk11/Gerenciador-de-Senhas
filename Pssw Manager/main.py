import sqlite3
import string
import random

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
    print(' *4* para gerar uma nova senha')
    print(' *5* para apagar algum servico')    
    print(' *6* para trocar uma senha ou username')
    print(' *0* para fechar o menu')
    print('-----------------------------------------')


def peg_senha(service):
    pass

def trocar_username(username):
    cursor.execute(f'''
        UPDATE users
        SET username = '{username}'
    ''')

def trocar_password(password):
    cursor.execute(f'''
        UPDATE users
        SET password = '{password}'
            ''')

def apagar_service(service):
    cursor.execute(f'''
        DELETE FROM users 
        WHERE service = '{service}'
    ''')

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

lista = []

while True:
    menu()
    selecionar = input("Selecione um numero para continuar: ")
    if selecionar not in ['1', '2', '3','4','5','6', '0']:
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
        lista.append(service)

    if selecionar == '2':
        mostrar_servicos()

    if selecionar == '3':
        service = input("Qual servico voce deseja ver a senha? ")
        mostrar_senha(service)
    
    if selecionar == '4':
        print('Gerando uma senha..')
        n_senhas = 1
        l_senhas = 12
        for x in range(n_senhas):
            senha_criada = print(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(l_senhas)))

    if selecionar == '5':
        service_delete = input("Qual servico voce deseja apagar? ")
        apagar_service(service_delete)
        lista.remove(service_delete)

    if selecionar == '6':                                                              
        service_select = input("Qual servico voce deseja trocar? ")
        if service_select not in lista:
            print('Selecione um servico valido')
        else:
            print('-----------------------------------------')
            service_troc = input('*1* Para trocar o username \n*2* Para trocar a senha\n ')
            print('-----------------------------------------')

            if service_troc == '1':
                username_new = input("Qual o novo username? ")
                trocar_username(username_new)

            if service_troc == '2':
                pssw_new = input("Qua a nova senha? ")
                trocar_password(pssw_new)


connect.close()



