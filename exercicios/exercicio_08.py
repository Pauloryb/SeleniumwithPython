''' Faça um programa que receba uma data de nascimento (15/07/87) e imprima:
'Você nasceu em <dia> de <mês> de <ano>'.'''

resposta = input ('Qual a sua data de nascimento? ')

dia, mes, ano = resposta .split('/')

print(f'Você nasceu em {dia} de {mes} de {ano}')
