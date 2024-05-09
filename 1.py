print('CONVERSOR DE TEMPERATURA - Celsius/Fahrenheit')
operacao = int(input('1 - Celsius para Fahrenheit\n2 - Fahrenheit para Celsius \n'))
if operacao == 1:
    celsius = int(input('Graus celsius: '))
    fahrenheit = (celsius * 1.8) + 32
    print(f'Sua temperatura em Fahrenheit é: {fahrenheit}')
elif operacao == 2:
    fahrenheit = int(input('Graus Fahrenheit: '))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f'Graus Celsius: {celsius}')
else:
    print('Operação inválida. Escolha entre 1 ou 2')

