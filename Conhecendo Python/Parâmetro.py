#Usando parametro em uma função

nome = 'João'

def saudacao_com_parametro(nome_da_pessoa):
    print(f'Olá {nome_da_pessoa}')

saudacao_com_parametro(nome)

###############################################################

#Condicional
#Verificar a idade se é possível dirigir

idade = 20
def verificaDirigir(idade_pessoa):
    if idade_pessoa < 18:
        print('Não é permitido dirigir')
    else:
        print('Permiti dirigir')  

verificaDirigir(idade) 

###############################################################

# Receber um valor dentro de uma função
def verificaDirigirsemParametro():
    idade = input('Qual sua idade? ')
    #Convertendo um tipo Int
    idade = int(idade)

    if idade < 18:
        print(f'{idade} anos Não tem permissão para dirigir')
    else:
        print(f'{idade} Tem permissão para dirigir')
        
verificaDirigirsemParametro()