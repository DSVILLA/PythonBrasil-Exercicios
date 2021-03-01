#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

horas = float(input('Quanto você ganha por hora? '))
mes = float(input('Quantas horas trabalhou por mês? '))
soma = horas * mes
print('Seu salário do mês é: R${:.2f}'.format(soma))