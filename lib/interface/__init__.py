import uuid
import hashlib

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError, NameError):
            print('\033[31mErro: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário prefereriu não digitar esse número.\033[m')
            return 0
        else:
            return n

def linha(tam=120):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(120))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL \n\n O que deseja fazer?')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc


def hash_message(message):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode()+message.encode()).hexdigest()+":"+salt

def check_message(hashed_message,user_message):
    message, salt = hashed_message.split(':')
    return message == hashlib.sha256(salt.encode()+user_message.encode()).hexdigest()

