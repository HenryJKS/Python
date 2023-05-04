#Crie uma função que imprime a quilometragem média anual de cada veículo em um dicionário

dados = {
    'Crossfox': {'km': 35000, 'ano': 2005}, 
    'DS5': {'km': 17000, 'ano': 2015}, 
    'Fusca': {'km': 130000, 'ano': 1979}, 
    'Jetta': {'km': 56000, 'ano': 2011}, 
    'Passat': {'km': 62000, 'ano': 1999},
    'GTR': {'km': 92033, 'ano': 2013}
}

def mediakm(dataset, data_inicial):
    result = {}
    for modelo, valores in dataset.items():
        media = round(valores['km'] / (data_inicial - valores['ano']),2)
        result.update({modelo : {'KM' : valores['km'], 'Média' : media}})
    return result

#Retorna um tipo dicionário
print(mediakm(dados, 2023))