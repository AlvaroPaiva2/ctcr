print('Digite 1 ou 0 para posicionar as alavancas')
alavanca1 = int(input('Digite a posição da alavanca 1: '))
alavanca2 = int(input('Digite a posição da alavanca 2: '))

if alavanca1 == 0 and alavanca2 == 0:
    print('Caminho C')
elif alavanca1 == 0 and alavanca2 == 1:
    print('Caminho C')
elif alavanca1 == 1 and alavanca2 == 1:
    print('Caminho A')
elif alavanca1 == 1 and alavanca2 == 0:
    print('Caminho B')
else:
    print('Por favor, escolha 0 ou 1')
