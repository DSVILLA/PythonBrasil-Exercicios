#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
pi = 3.14
print('Calculando o raio de um circulo e mostrando sua área!')
raio = float(input('Qual o raio do circulo: '))
area = pi * (raio * raio)
print('A área é de: {:.2f}'.format(area))
