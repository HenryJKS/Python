#Loops

idades = [10]

def verifica_idade(idade):
    if idade < 18:
        print(f' {idade} anos de idade é Permitido dirigir')
    else:
        print(f' {idade} anos de idade Não é permitido dirigir')

#Verificar toda lista de Idades e se dentro da função verifica_idade, são permitido a dirigir
    for idade in idades:
        verifica_idade(idades)


#Loop dentro de uma função
def verifica(idades):
    for idade in idades:
        if idade < 18:
            print(f'{idade} anos de idade é permitido dirigir')
        else:
            print(f'{idade} anos de idade nao é permitido dirigir')

    verifica(idades)