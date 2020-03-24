#Importar biblioteca criada com funcoes
from aps.lib.interface import*
#Importar arquivos criados
from aps.lib.arquivo import*
# Importar tempo de andamento do sistema
from time import sleep


arq = 'crip.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

criptada = ''
msgcript = ''
lista = []

cabeçalho(' APS DE CRIPTOGRAFIA 2º SEMESTRE UNIP')
cabeçalho('Bem vindo ao nosso Programa')
print('')
print('')
nome = ''

nome = input('Olá, me diga seu nome: ')
print(f'\nVamos dar inicio a sua experiência digite 1 para começar {nome}'.upper())


while True:
    resposta = menu(['Criptografar','Descriptografar','Ver criptografia','Sair do sistema '])

    if resposta == 1:
        cabeçalho('Digite sua mensagem: ')
        criptada = input('Digite aqui: ')
        print('')
        hashed_message = hash_message(criptada)
        print(f'\033[32mMensagem criptografada: \033[m', hashed_message)
        f = open('crip.txt','w')
        for i in range(0, len(criptada)):
            lista.append(criptada)
            f.write(criptada)
        cabeçalho('Crie uma senha:')
        senha = input('Senha:  ')
        lista.append(senha)
        f.close()

    elif resposta == 2:
        cabeçalho('Digite sua senha:')
        check = input(' ')
        if check == senha:
            print('\033[32mSua mensagem digita foi:\033[m ', criptada)
        else:
            print('\033[31msenha incorreta !\033[m')

    elif resposta == 3:
        print('\033[32mSua mensagem encriptada é:\033[m ', hashed_message)

    elif resposta == 4:
        cabeçalho('Saindo do sistema ... Até logo!')
        cabeçalho('Um agradecimento especial de:\n DANIEL RABELO\n DJAVAN CLAUDIO\n LUCAS SILVA\n RENAN COELHO\n VINICIUS VAZ')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
