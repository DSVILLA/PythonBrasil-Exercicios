#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o
# rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento
# de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite e na variável
# multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.

produto = float(input('Qual o peso dos peixes? '))
excesso = produto - 50
multa = excesso * 4.00

if produto <= 50:
    print('Você está dentros dos limites estabelecidos! O peso é de {}Kg o que não ultrapassa os 50Kg.'.format(produto))

else:
    print('Você excedeu o limite, terá de pagar uma multa total de R${}, para os {}Kg de peixes a mais.'.format(multa, excesso))
