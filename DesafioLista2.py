#OUTPUT: ['Airbag','Ar condicionado','Bancos de couro','Piloto automático','Rodas de liga','Vidros elétricos']

Acessorios = [
    'Rodas de liga', 
    'Travas elétricas', 
    'Piloto automático',
    'Bancos de couro',
    'Ar condicionado'
]

Acessorios.append('Airbag')
Acessorios.sort()
Acessorios.pop()
Acessorios.append('Vidros elétricos')
print(Acessorios)