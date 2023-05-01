import numpy as np

idades = np.array([10, 23, 45, 34, 25])


idades_somatoria = np.sum(idades) 
idades_tamanho = np.size(idades)

idade_media = idades_somatoria / idades_tamanho
print(idade_media)

print(idades.mean())