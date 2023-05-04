#Dicionários são coleções poucos diferentes, são estruturas de dados que representam um tipo de mapeamento.

#Mapeamento são coleções de associações entre pares de valores onde o primeiro elemento par de elemento é conhecido como "KEY" e o segundo valor como "VALUE"

#Sintaxe: {value1 : value2}

carros = ['Jetta Variant', 'Passat', 'Crossfox']
valores = [88078.64, 106161.94, 72832.16]

#Verificar qual index está cada valor
carros.index('Passat')

#Verificar o preço do index valores com o index de carros
valores[carros.index('Passat')]

#Podemos melhorar esses processos usando "DICIONARIOS"

#Criando Dicionario
dados = {'Jetta Variant' : 88078.64, 'Passat' : 106161.94, 'Crossfox' : 72832.16}

#Criando Dicionario com ZIP (COM ZIP EVITAMOS ESCREVER MAIS)
dados2 = dict(zip(carros, valores))

