#Funções sem parametros
#SINTAXE "def <nome>():"
#         <instruções>

#Criando função sem parametros
def media():
    valor = (1 + 2 + 3) / 3
    return valor

#Chamando a função
media()

#Criando função com parametros
def mediaparametro(lista):
  valor = sum(lista) / len(lista)
  #o retorno é do valor e o tamanho da lista
  return (valor, len(lista))


#chamando a função com 2 retornos, assim consigo ter uma tupla, com o valor e o "len(lista)"
#posso separar essa tupla com 2 variaveis
resultado, tamanho = mediaparametro([1, 2, 3, 4, 5])
print(mediaparametro ([1, 2, 3, 4, 5]))
print(resultado)
print(tamanho)




