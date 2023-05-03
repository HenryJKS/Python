#E utilizando o ferramental apresentado acima, marque a alternativa com o código que possibilita a impressão dos nomes dos veículos com quilometragem abaixo de 20.000 km.

kms = [15000, 12000, 32000, 8000, 50000]
nomes = ['Passat', 'Crossfox', 'DS5', 'C4', 'Jetta']

for km, nome in zip(kms, nomes):
    if km < 20000:
        print(nome, km)