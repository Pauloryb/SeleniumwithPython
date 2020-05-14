
carteira = int(input('Quanto eu tenho? '))
tenis = int(input('Quanto custa? '))
necessidade = input('Precisa mesmo disso [s/n]? ')

if carteira >= tenis and necessidade == 's':
    print('Beleza, comprei um novo tenis!')
else:
    print('É, deixa para o mês que vem!')
