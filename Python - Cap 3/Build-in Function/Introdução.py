dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}

valores = []

#Soma dos valores de um dicionario

#Acessando os valores
for valor in dados.values():
    #Adicionando os valors em um variavel "valores"
    valores.append(valor)

#Usando funçao sum
print(sum(valores))
