#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o
# Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo

horas = float(input('Quanto você ganha por hora? '))
mes = float(input('Quantas horas você trabalhou este mês? '))

sal_bruto = horas * mes
imposto = (sal_bruto * 11 / 100)
inss = (sal_bruto * 8 / 100)
sind = (sal_bruto * 5 /100)
final = sal_bruto - (imposto + inss + sind)
print('Seu salário bruto é de R${}'.format(sal_bruto))
print('Você irá pagar R${:.1f} de imposto de renda!'.format(imposto))
print('Você irá pagar R${:.1f} para o INSS!'.format(inss))
print('E você pagará R${:.1f} para o sindicato!'.format(sind))
print('Seu salário com todos os descontos é de: R${}'.format(final))
