#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
a = float(input('Digite a altura do quadrado: '))
l = float(input('Digite a largura do quadrado: '))
dobro = a * l
print('O dobro desta área é: {:.2f}m2'.format(dobro * 2))
