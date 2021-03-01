#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
f = float(input('Quantos graus Fahrenheit está agora? '))
c = 5 * ((f-32) / 9)
print('A coversão de Fahrenheit para graus Celsius é de: {:.1f}Cª!'.format(c))
