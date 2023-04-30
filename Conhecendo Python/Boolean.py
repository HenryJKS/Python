# Tipo Booleana

permissoes = []
idades = [20, 14, 40]

def verifica_pode_dirigir(idades, permissoes):
    for idade in idades:
        if idade >= 18:
            #Adicionar o valor True na lista de permissoes
            permissoes.append(True)
        else:
            #Adicionar o valor False na lista de permissoes
            permissoes.append(False)
verifica_pode_dirigir(idades, permissoes)
print(permissoes)

#Com valores na lista de permissoes, podemos usar para verificar se pode ou não dirigir
for permissao in permissoes:
    if permissao == True:
        print('tem permissão para dirigir')
    else:
        print('não tem permissão para digirir')



