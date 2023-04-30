# Operador For

Acessorios = ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']

quadrado = []

#Para cada item em acessorios
for item in Acessorios:
    print(item)

#Um for para inserir em uma lista
for i in range(10):
    quadrado.append(i ** 2)

#Outra forma sem usar variavel
(i ** 2 for i in range(10))



