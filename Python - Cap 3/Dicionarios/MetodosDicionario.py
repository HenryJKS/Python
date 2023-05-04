dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}

#Incluindo dados
dados['DS5'] = 124549.07

#Deletando dados
del dados['Passat']

#Atualiza dicionario
dados.update({'Passat' : 106161.94, 'Fusca' : 150000})

#Cria uma cópia do dicionario
dadosCopy = dados.copy()

#"POP" o item é removido e seu valor é retornado, caso contrário o valor especificado como default é retornado.
dadosCopy.pop('Passat')
dadosCopy
dadosCopy.pop('Passat', 'Chave não encontrada')

#Limpar dicionarios
dadosCopy.clear()
