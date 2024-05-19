# print('CONVERSOR')
# #req input
# segundos = int(input('Digite a quantidade de segundos: '))
# #logica
# dia = int(segundos / 86400)
# restoDia = int(segundos % 86400)
# hrs = int(restoDia / 3600)
# restoHoras = int(restoDia % 3600)
# mnts = int(restoHoras / 60)
# secs = int(restoHoras % 60)
# #decisoes
# if dia > 1:
#     print(f'{dia} dias, {hrs}h, {mnts}m e {secs} segundos')
# else:
#     print(f'{dia} dia, {hrs}h, {mnts}m e {secs} segundos')

# a = int(input("Qual o valor de a? "))
# b = int(input("Qual o valor de b? "))
# aux = a
# a = b
# b = aux
# print(a)
# print(

# dia = int(input('Digite a quantidade de dias: '))
#
# match dia:
#     case dia if 1 <= dia <= 30:
#         print(f'um mes!')
#     case _:
#         print(f'fudeu')
#
#
# print('pergunta 01')
# answer = input('Com quantos paus se faz uma canoa?\n'
#                'a) 3\n'
#                'b) 4\n'
#                'c) 5\n'
#                'd) 6\n')
# match answer:
#     case 'a':
#         print('Resposta errada')
#     case 'b':
#         print('Resposta correta')
#     case 'c':
#         print('Resposta errada')
#     case 'd':
#         print('ta de sacanagem?')
#     case _:
#         print('Resposta invalida')

nome = input('Digite seu nome: ')
gostaNome = str(input(f'Olá, {nome.capitalize()}! Você gosta do seu nome? '))
if gostaNome == 'sim' or 'Sim' or 'SIM' or 's' or 'S':
    print('Que bom!')
else:
    print('Que pena!')


























