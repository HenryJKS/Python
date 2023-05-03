#Iterando com Tuplas

nome_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5')


for item in nome_carros:
    item

#Desempacotamento de Tuplas
carro1, carro2, carro3, carro4 = nome_carros


#Desempacotamento de algumas variaveis
_, A, *_ = nome_carros

#BuildFunction ZIP
#o ZIP cria iterador com tuplas
carros = ['Jetta Variant', 'Passat', 'Crossfox', 'DS5']
valores = [88078.64, 106161.94, 72832.16, 124549.07]

#Com isso podemos criar um lista com o iterador
list(zip(carros, valores))

#Ou podemos:
for item in zip(carros, valores):
    item

#Podemos separar os valores também:
for carro, valor in zip(carros, valores):
    if valor > 100000:
        print(carro, valor)