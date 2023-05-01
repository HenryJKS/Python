#Desafio 01
#Marque a alternativa que mostra o código que permite a seleção, sem utilização de operadores lógicos (and e or), das informações de nome e estado civil, somente das pessoas do sexo masculino.
import numpy as np

dados = np.array(
    [
        ['Roberto', 'casado', 'masculino'],
        ['Sheila', 'solteira', 'feminino'],
        ['Bruno', 'solteiro', 'masculino'],
        ['Rita', 'casada', 'feminino']
    ]
)

#Começando a varredura no indice 0 e pulando de 2 casas nas colunas, e nas linhas queremos somentes o indicie 0 e 1
print(dados[0::2, :2])