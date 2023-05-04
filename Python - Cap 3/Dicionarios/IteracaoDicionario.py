dados = {'Crossfox': 72832.16, 'DS5': 124549.07,  'Fusca': 150000,  'Jetta Variant': 88078.64,  'Passat': 106161.95}

#"keys()" retorna uma lista com as chaves do dicionario
dados.keys()

for key in dados.keys():
    print(dados[key])

#"values()" retorna uma lista com valores do dicionarios
dados.values()

#"items" retorna uma tupla para cada par chave-valor
dados.items()

#Podemos desempacotear também
for key, value in dados.items():
    print(key, value)

#Podemos usar uma condição
for key, value in dados.items():
    if value > 100000:
        print(key)