#Faça um Programa que converta metros para centímetros.

print('Metros em centimetros! ')
m = float(input('Digite os metros: '))
conversao = m * 100
print('{:.1f}Metros tem: {:.1f}cm! '.format(m, conversao))