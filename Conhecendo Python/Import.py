#Import para gerar números aleatorios

from random import randrange
from random import seed
import random


notas_matematica = []

for notas in range(9):
    notas_matematica.append(randrange(0, 11))

print(notas_matematica)


