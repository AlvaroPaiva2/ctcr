segundos = int(input('Por favor, entre com o número de segundos que deseja converter: '))

dia = int(segundos / 86400)
restoDia = int(segundos % 86400)
horas = int(restoDia / 3600)
restoHoras = int(restoDia % 3600)
minutos = int(restoHoras / 60)
secs = int(restoHoras % 60)

print(f'{dia} dias, {horas} horas, {minutos} minutos e {secs} segundos.')