from datetime import date
nasc = int(input('Ano de nascimento: '))
ano = date.today().year
idade = ano - nasc
print('Você nasceu em {} e tem {} anos em {}' .format(nasc, idade, ano))
if idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos, ainda faltam {} anos para o alistamento' .format(saldo))
elif idade == 18:
    print('Você tem 18 anos, esta na hora de se alistar!')
elif idade > 18:
    saldo = idade - 18
    print('Você já passou da idade de se alistar, ja se passaram {} anos do seu alistamento' .format(saldo))
