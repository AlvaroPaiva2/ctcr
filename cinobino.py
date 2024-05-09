nota1 = float(input())
nota2 = float(input())
media = float((nota1 + nota2) / 2)
if media > 4 and media < 7:
    print('Recuperacao')
elif media >= 7:
    print('Aprovado')
else:
    print('Reprovado')