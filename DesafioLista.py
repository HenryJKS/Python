#Printe os seguintes itens:
#1) True
#2) 'Teto panorâmico'
#3) ['Rodas de liga', 'Travas elétricas', 'Piloto automático']

carros = [
    [
        'Jetta Variant',
        'Motor 4.0 Turbo',
        2003,
        False,
        ['Rodas de liga', 'Travas elétricas', 'Piloto automático']
    ],
    [
        'Passat',
        'Motor Diesel',
        1991,
        True,
        ['Central multimídia', 'Teto panorâmico', 'Freios ABS']
    ]
]

print(carros[1][3])
print(carros[1][-1][-2])
print(carros[0][-1])