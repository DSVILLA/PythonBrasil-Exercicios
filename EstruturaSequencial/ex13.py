#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

resp = str(input('Você é homem ou mulher? Responda com F ou M! '))
receveid_message = resp.upper()
if receveid_message == 'M':
    a = float(input('Qual a sua altura? '))
    peso_1 = (72.7 * a) -58
    print('Seu peso ideal é: {:.1f}Kg'.format(peso_1))
if receveid_message == 'F':
    b = float(input('Qual a sua altura? '))
    peso_2 = (62.1 * b) - 44.7
    print('Seu peso ideal é: {:.1f}Kg'.format(peso_2))
