''' Faça um programa que itera em uma string a toda vez que uma vogal aparecer
na sua string print o seu nome entre as letras.'''

'''
# Exemplo
palavra = 'abracadabra'

for letra in palavra:
    if letra == 'a':
        print('Paulo')
    elif letra == 'e':
        print('Paulo')
    elif letra == 'i':
        print('Paulo')
    elif letra == 'o':
        print('Paulo')
    elif letra == 'u':
        print('Paulo')
    else:
        print(letra)
'''
palavra = 'abracadabra'
vogais = 'aeiou'

for letra in palavra:
    if letra in vogais:
        print('Paulo')
    else:
        print(letra)
