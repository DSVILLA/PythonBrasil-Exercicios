#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

c = float(input('Digite a temperatura atual em graus Celsius: '))
f = (c * 9 / 5) +32
print('A conversão da temperatura de Celsius para Fahrenheit é de: {:.2f}Fº!'.format(f))
