# Operador if
# 1º item da lista - Nome do veículo
# 2º item da lista - Ano de fabricação
# 3º item da lista - Veículo é zero km?

dados = [
    ['Jetta Variant', 2003, False],
    ['Passat', 1991, False],
    ['Crossfox', 1990, False],
    ['DS5', 2019, True],
    ['Aston Martin DB4', 2006, False],
    ['Palio Weekend', 2012, False],
    ['A5', 2019, True],
    ['Série 3 Cabrio', 2009, False],
    ['Dodge Jorney', 2019, False],
    ['Carens', 2011, False]
]

#Verificar os carros, se for true coloque em um varizel zero_km senão coloque em uma variavel nao_zerokm
nao_zero_km = []
zero_km = []
for carros in dados:
    if carros[2] == True:
        zero_km.append(carros)
    else:
        nao_zero_km.append(carros)

#Verificar o ano do carro, se o carro for <= a 2000 insira na variavel A, se for > 2000 e <= 2010 insria na variavel b, senão inseria na variavel c
A = []
B = []
C = []

for ano in dados:
    if ano[1] <= 2000:
        A.append(ano)
    elif ano[1] > 2000 and ano[1] <= 2010:
        B.append(ano)
    else:
        C.append(ano)

