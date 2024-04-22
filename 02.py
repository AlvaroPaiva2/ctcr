# exercicio 2 - Calculadora básica
print('=== CALCULADORA ===')
# requisições de input
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
operacao = input('Digite a operação desejada: ')
# operações matemáticas básicas
if operacao == '+':
    soma = int(num1 + num2)
    print('A soma dos números é: ', soma)
elif operacao == '-':
    subtracao = int(num1 - num2)
    print('A subtração dos números é: ', subtracao)
elif operacao == '*':
    multiplicacao = int(num1 * num2)
    print('A multiplicação dos números é: ', multiplicacao)
# divisão com tratamento de divisão por zero, OBRIGATORIO
elif operacao == '/':
    if num2 != 0:
        divisao = int(num1 / num2)
    print('A divisão dos números é: ', divisao)
# operação inválida
else:
    print('Operação inválida.')

