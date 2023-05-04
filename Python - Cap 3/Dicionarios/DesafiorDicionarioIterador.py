#Selecione a alternativa que apresenta o código que imprime somente os nomes dos veículos com ano de fabricação maior ou igual a 2000.

dados = {
    'Crossfox': {'valor': 72000, 'ano': 2005}, 
    'DS5': {'valor': 125000, 'ano': 2015}, 
    'Fusca': {'valor': 150000, 'ano': 1976}, 
    'Jetta': {'valor': 88000, 'ano': 2010}, 
    'Passat': {'valor': 106000, 'ano': 1998}
}

print(dados.items())

for key, values in dados.items():
    if values['ano'] >= 2000:
        print(key, values['ano'])


