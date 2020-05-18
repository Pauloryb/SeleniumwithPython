# Exemplo 1
'''resposta = input('Vamos sair hoje [s/n]? ')

while resposta != 's':
    resposta = input('Vamos [s/n]? ')
print('Então, vamos!!')
'''

# Exemplo 2

resposta = input('Vamos sair hoje [s/n]? ')

n = 1

while resposta != 's':

    resposta = input(f'Vamos{"s" * n} [s/n]? ')
    n += 1   # [n += 1] é igual a [n = n + 1]
    if 'chato' in resposta or 'chata' in resposta:
        print('Desculpa, foi mal')
        break
else:
    print(f'Então, vamos{"s" * n}!!')
