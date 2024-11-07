import sys
import os
sys.path.append(os.path.abspath(os.curdir))

from model.password import Password
from views.view_password import FernetHasher


action = input("Digite 1 para salvar uma nova senha ou 2 para ver uma senha já salva:")

if action == '1':
    if len(Password.get()) == 0:
        key, path = FernetHasher.create_key(archive=True)
        print('Sua chave foi gerada com sucesso:)\nSalve-a com cuidado!')
        print(f'Chave: {key.decode("utf-8")}')
        if path:
            print("Chave salva no arquivo, lembre-se de remover o arquivo após transferir do local")
            print(f'Caminho {path}')
    
    else:
        key = input("Insira a chave usada para criptografia (utilize sempre a mesma chave)")
        
    domain = input("Insira o domínio:")
    password = input("Digite a senha:")
    fernet_user = FernetHasher(key)
    p1 = Password(domain=domain, password=fernet_user.encrypt(password).decode('utf-8'))
    p1.save()


elif action == '2':
    domain = input("Digite o domínio: ")
    key= input("Digite a chave: ")
    fernet_user= FernetHasher(key)
    data = Password.get()

    for i in data:
        if domain in i['domain']:
            password = fernet_user.decrypt(i['password'])
        if password:
            print(f"Sua senha: `{password}")
        else:
            print("Nehuma senha foi encontrada para esse domínio :()")
