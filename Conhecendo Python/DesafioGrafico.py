#Criando um grafico com notas randomizadas
#Notas para Mat, Port e Geo
#Listar 8 Provas e 8 Notas

import matplotlib.pyplot as plt
from random import randrange

notas_matematica = ['Matematica']
notas_portugues = ['Portugês']
notas_geografia = ['Geografia']

for notas_geral in range(8):
    notas_matematica.append(randrange(0, 11))
    notas_portugues.append(randrange(0, 11))
    notas_geografia.append(randrange(0, 11))

notas = [notas_matematica, notas_portugues, notas_geografia]

print(notas_matematica)
print(notas_portugues)
print(notas_geografia)

for nota in notas:
    x = list(range(1, 9))
    y = nota[1:]
    plt.plot(x, y, marker = 'o')
    plt.xlabel('Provas')
    plt.ylabel('Notas')
    plt.title(nota[0])
    plt.show()