#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#   a- produto do dobro do primeiro com metade do segundo .
#   b- soma do triplo do primeiro com o terceiro.
#   c- terceiro elevado ao cubo.

var_a = int(input('Digite um número inteiro: '))
var_b = int(input('Digite um número inteiro: '))
var_c = float(input('Digite um número real: '))

s1 = (var_a * 2) + (var_b / 2)
s2 = (var_a * 3) + var_c
s3 = var_c * 3

print('O produto do dobro do primeiro número com metade do segundo é: {:.2f}'.format(s1))
print('A soma do triplo do primeiro com o terceiro é: {}'.format(s2))
print('O terceiro elevado ao cubo é: {}'.format(s3))


