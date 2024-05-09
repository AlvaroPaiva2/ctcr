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
# print('=== Calculadora de valores ===')
# excesso = print('Excesso de peso: o que passa de 50kg')
# multa = print('Multa: R$ 4,00 por kg excedente')
# peso = float(input('Digite o peso dos peixes em kg: '))
# if peso > 50:
#         excesso = peso - 50
#         multa = excesso * 4
#         print(f'Excesso de peso: {excesso:.2f} kg')
#         print(f'Multa: R$ {multa:.2f}')
# else:
#         print('Peso dentro do limite permitido.')

# Exercicios de Python 11
# coleta informações do usuário
# print('=== Gasto mensal do funcionario ===')
# salarioPorHora = float(input('Quanto você ganha por hora? '))
# horasTrabalhadasPorMes = float(input('Quantas horas você trabalhou esse mês? '))
# # calcula o salário bruto, imposto de renda, INSS, sindicato e salário líquido
# salarioBruto = salarioPorHora * horasTrabalhadasPorMes
# impostoRenda = salarioBruto * 0.11
# if salarioBruto <= 900:
#     impostoRenda = str('Isento de imposto de renda')
# else:
#     impostoRenda = float(salarioBruto * 0.11)
# inss = salarioBruto * 0.08
# sindicato = salarioBruto * 0.05
# salarioLiquido = salarioBruto - inss - sindicato
# if impostoRenda == 'Isento de imposto de renda':
#     salarioLiquido = salarioBruto - inss - sindicato
# else:
#     salarioLiquido = salarioBruto - impostoRenda - inss - sindicato
# # imprime os valores
# print(f'\n + Salário Bruto: {str(salarioBruto)} '
#       f'\n - IR (11%):  {str(impostoRenda)} '
#       f'\n - INSS (8%): {str(inss)} '
#       f'\n - Sindicato (5%): {str(sindicato):} '
#       f'\n = Salário Líquido: {str(salarioLiquido)}')

# Exercicios de Python 12
# print('=== loja de tinta ===')
# area = float(input('Digite a área a ser pintada em m²: '))
# litros = area / 3
# if litros < 18:
#     litros = 18
#     latas = 1
# else:
#     latas = litros / 18
#     latas = int(latas + 1)
# preco = latas * 80
# print(f'Você precisará de {latas} latas de tinta.')
# print(f'O preço total é R$ {preco:.2f}')

# Exercicios de Python 13
# print('===  ===')
# area = float(input('Digite a área a ser pintada em m²: '))
# litros = area / 3
# if litros < 18:
#      litros = 18
#      latas = 1
# else:
#     latas = litros / 18
#     latas = int(latas + 1)
#  preco = latas * 80
# print(f'Você precisará de {latas} latas de tinta.')
# print(f'O preço total é R$ {preco:.2f}')

# Exercicios de Python 14
# print('=== pede-numero-e-mostra-o-maior ===')
# numero1 = int(input('Digite um número: '))
# numero2 = int(input('Digite outro número: '))
# if numero1 > numero2:
#     print(numero1)
# else:
#     print(numero2)

# Exercicios de Python 15
# print('=== positivo ou negativo? ===')
# numero = int(input('Digite um número: '))
# if numero > 0:
#     print('Positivo')
# else:
#     print('Negativo')

# Exercicios de Python 16 - muito parecido com um anterior
# print('=== folha de pagamento ===')
# #requisições de input
# salarioHora = float(input('Quanto você ganha por hora? '))
# horasTrabalhadas = float(input('Quantas horas você trabalhou esse mês? '))
# #calculos
# salarioBruto = salarioHora * horasTrabalhadas
# impostoRenda = 0
# if salarioBruto <= 900:
#         impostoRenda = str('Isento de imposto de renda')
# elif salarioBruto > 900 and salarioBruto <= 1500:
#         impostoRenda = salarioBruto * 0.05
# elif salarioBruto > 1500 and salarioBruto <= 2500:
#         impostoRenda = salarioBruto * 0.10
# else:
#         impostoRenda = salarioBruto * 0.20
# fgts = salarioBruto * 0.11
# inss = salarioBruto * 0.10
# salarioLiquido = salarioBruto - inss + fgts
# if impostoRenda == 'Isento de imposto de renda':
#     salarioLiquido = salarioBruto - inss + fgts
# else:
#     salarioLiquido = salarioBruto - impostoRenda - inss + fgts
# #imprime os valores
# print(f'\n + Salário Bruto: {str(salarioBruto)} '
#       f'\n + FGTS (11%): {str(fgts)} '
#       f'\n - IR (5%, 10% ou 20%): {str(impostoRenda)} '
#       f'\n - INSS (10%): {str(inss)} '
#       f'\n = Salário Líquido: {str(salarioLiquido)}')

# Exercicios de Python 17
# print('=== maior e menor numero ===')
# num1 = float(input('Digite um número: '))
# num2 = float(input('Digite outro número: '))
# num3 = float(input('Digite outro número: '))
# if num1 > num2 and num1 > num3 and num2 > num3:
#     print(f'{num1} é o maior número e {num3} é o menor número.')
# elif num1 > num2 and num1 > num3 and num3 > num2:
#     print(f'{num1} é o maior número e {num2} é o menor número.')
# elif num2 > num1 and num2 > num3 and num1 > num3:
#     print(f'{num2} é o maior número e {num3} é o menor número.')
# elif num2 > num1 and num2 > num3 and num3 > num1:
#     print(f'{num2} é o maior número e {num1} é o menor número.')
# elif num3 > num1 and num3 > num2 and num1 > num2:
#     print(f'{num3} é o maior número e {num2} é o menor número.')
# elif num3 > num1 and num3 > num2 and num2 > num1:
#     print(f'{num3} é o maior número e {num1} é o menor número.')
# else:
#     print('Os números são iguais.')

# Exercicios de Python 18
# print('===  ===')
# # função para obter um número maior que 0
# def obter_numero():
#     while True:
#         numero = float(input('Digite um número: '))
#         if numero > 0:
#             return numero
#         else:
#             print('Por favor, digite um número maior que 0.')
# # obtem os números
# numero1 = obter_numero()
# numero2 = obter_numero()
# numero3 = obter_numero()
# # verifica qual é o maior número
# if numero1 > numero2 and numero1 > numero3:
#     print(f'{numero1} é o maior número.')
# elif numero2 > numero1 and numero2 > numero3:
#     print(f'{numero2} é o maior número.')
# else:
#     print(f'{numero3} é o maior número.')

# Exercicios de Python 19
#print('===  ===')






























































