#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
print('-=-' * 20)
print('NOTAS BIMESTRAIS')
print('-=-' * 20)
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))
media = n1 + n2 + n3 + n4 / 3
print('Sua média é: {}'.format(media))
