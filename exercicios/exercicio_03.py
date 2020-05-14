''' Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
 em metros quadrados da área a ser pintada. Considere que a cobertura da tinta
 é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
 18 litros, que custa R$80,00. Informe ao usuário a quantidade de latas de tinta
 a serem compradas e o preço total. '''

tamanho1 = float(input('Informe o tamanho em metros quadrados da area a ser pintada: '))

#lata1 = round((tamanho1/3)/18)
lata1 = (tamanho1/3)/18
precototal = lata1*80

print(f'Será necessário comprar {lata1} lata(s) no valor total de R${precototal}')
