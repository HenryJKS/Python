#Queremos o seguinte:
#1) Testar se a chave acessorios existe no dicionário de informações do carro Crossfox (Resposta: False)
#2) Testar se a chave acessorios existe no dicionário de informações do carro Passat (Resposta: True)
#3) Obter o valor do carro Crossfox (Resposta: 25000)
#4) Acessar o último acessório do carro Passat (Resposta: 'ABS')

dados = {
    'Passat': {
        'ano': 2012,
        'km': 50000,
        'valor': 75000,
        'acessorios': ['Airbag', 'ABS']
    }, 
    'Crossfox': {
        'ano': 2015,
        'km': 35000,
        'valor': 25000
    }
}

print('acessorios' in dados['Crossfox'])
print('acessorios' in dados['Passat'])
print(dados['Crossfox']['valor'])
print(dados['Passat']['acessorios'][-1])

