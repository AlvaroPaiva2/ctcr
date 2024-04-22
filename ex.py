# Exercicios de Python 1
# print('=== SITUAÇÃO FINAL DO ALUNO ===')
# def obter_nota(bimestre):
#     while True:
#         nota = float(input(f'{bimestre} bimestre: '))
#         if 0 <= nota <= 10:
#             return nota
#         else:
#             print("Por favor, digite um número entre 0 e 10.")
# nota1 = obter_nota('Primeiro')
# nota2 = obter_nota('Segundo')
# nota3 = obter_nota('Terceiro')
# nota4 = obter_nota('Quarto')
# media = (nota1 + nota2 + nota3 + nota4) / 4
# print('Média final: ', media)
# if media >= 7:
#    print('Aprovado com média: ', media)
# elif media >= 5 and media < 7:
#     print('Recuperação com média: ', media)
# else:
#     print('Reprovado com média: ', media)

# Exercicios de Python 02
# print('=== CONVERSOR DE METROS PARA CENTÍMETROS ===')
# metros = float(input('Metros: '))
# centimetros = metros * 100
# print(f'{metros} metros é igual a {centimetros} centímetros.')

# Exercicios de Python 03
# print('=== CALCULADORA DE ÁREA DE CÍRCULO ===')
# raio = float(input('Raio do círculo: '))
# area = 3.14 * (raio ** 2)
# print(f'A área do círculo é: {area}')

# Exercicios de Python 04
# print('=== CALCULADORA DE ÁREA DE TRIANGULO ===')
# def obter_lado():
#     while True:
#         lado = float(input('Lado do triangulo: '))
#         if lado > 0:
#             return lado
#         else:
#             print('Por favor, digite um número maior que 0.')
# lado1 = obter_lado()
# lado2 = obter_lado()
# lado3 = obter_lado()
# area = (lado1 + lado2 + lado3) / 2
# print(f'A área do triângulo é: {area}')

# Exercicios de Python 05
# print('=== MEU SALARIO MENSAL ===')
# salarioPorHora = float(input('Quanto você ganha por hora? '))
# horasTrabalhadas = float(input('Quantas horas você trabalha por mês? '))
# print(f'Seu salário mensal é: R$ {salarioPorHora * horasTrabalhadas:.2f}')

# Exercicios de Python 06
# print('=== Quantos Celsius estão fazendo? ===')
# tempFah = float(input('Digite a temperatura em Fahrenheit: '))
# tempCel = 5 * ((tempFah - 32) / 9)
# print(f'A temperatura em Celsius é: {tempCel:.2f}')

# Exercicios de Python 07
# print('=== 06/2 ===')
# tempCelsius = float(input('Digite a temperatura em Celsius: '))
# tempFah = (tempCelsius * 9/5) + 32
# print(f'A temperatura em Fahrenheit é: {tempFah:.2f}')

# Exercicios de Python 08
# print('=== conta maluca ===')
# numInt1 = int(input('Digite um número inteiro: '))
# numInt2 = int(input('Digite outro número inteiro: '))
# numReal1 = float(input('Digite um número real: '))
#
# operacaoA = float(numInt1 * numInt1 * 2 + (numInt2 / 2))
# operacaoB = float(numInt1 * 3 + numReal1)
# operacaoC = float(numReal1 * numReal1 * numReal1)
#
# print(f'\n {operacaoA:.2f} \n {operacaoB:.2f} \n {operacaoC:.2f}')

# Exercicios de Python 09
# print('=== peso ideal para mulheres e nao mulheres ===')
# genero = input('Digite seu gênero: ')
# altura = float(input('Digite sua altura: '))
# if genero == 'masculino':
#     pesoIdeal = float((72.7 * altura) - 58)
#     print(f'Seu peso ideal é: {pesoIdeal:.2f}')
# elif genero == 'feminino':
#     pesoIdeal = float((62.1 * altura) - 44.7)
#     print(f'Seu peso ideal é: {pesoIdeal:.2f}')
# else:
#     print('Gênero inválido.')

# Exercicios de Python 10
print('=== Calculadora de valores ===')
excesso = print('Excesso de peso: o que passa de 50kg')
multa = print('Multa: R$ 4,00 por kg excedente')
peso = float(input('Digite o peso dos peixes em kg: '))
if peso > 50:
        excesso = peso - 50
        multa = excesso * 4
        print(f'Excesso de peso: {excesso:.2f} kg')
        print(f'Multa: R$ {multa:.2f}')
else:
        print('Peso dentro do limite permitido.')





































