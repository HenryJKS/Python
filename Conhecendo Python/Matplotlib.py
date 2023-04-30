# um Import para criação de gráficos

import matplotlib.pyplot as plt
#Importando função de outra classe 
from Import import notas_matematica

#Lista de int de 1 ao 9
x = list(range(1,10))

print(x)
y = notas_matematica

#Gerar o gráfico
plt.plot(x,y, marker = 'o')

#Dar titulo a um grafico
plt.title('Notas Matematica')
#Dar titulo ao eixo x
plt.xlabel('Provas')
#Dar titulo ao eixo y
plt.ylabel('Notas')

#Mostrar o gráfico
plt.show()



