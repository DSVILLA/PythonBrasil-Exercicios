#Faça um programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de
# latas de tinta a serem compradas e o preço total.

m = float(input('Qual o metro quadrado a ser pintado? '))
litros = m / 3
lata = 18
pre_total = 80

latas = litros / lata
total = latas * pre_total

print('Você precisará de {:.1f} latas de tinta para pintar uma área de {:.1f}M'.format(latas, m))
print('Portanto custará R${:.1f}, as {:.1f}latas;'.format(total, latas))
