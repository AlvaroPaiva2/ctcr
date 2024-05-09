num1 = int(input('primeiro numero: '))
num2 = int(input('segundo numero: '))
num3 = int(input('terceiro numero: '))
if not(num1 > num2 > num3):
    print('crescente')
else:
    print('não está em ordem crescente')