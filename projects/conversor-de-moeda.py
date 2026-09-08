print("==="*20)
print('CONVERSOR DE MOEDA')
print('==='*20) 
print('''Informe qual moeda deseja converter:
[ 1 ] Dólar
[ 2 ] Euro
[ 3 ] Libra
[ 4 ] Reais\n''')
# PREÇO EM REAIS
dolar = 0.20
euro = 0.17
libra = 0.14
reais = 1.00
op1 = int(input('Digite a opção desejada: '))
if op1 == 1:
    moeda = 'Dólar'
elif op1 == 2:
    moeda = 'Euro'
elif op1 == 3:
    moeda = 'Libra'
elif op1 == 4:
    moeda = 'Reais'
else:
    print('\033[31mOpção invalida\033[m')
print('Converter de {}' .format(moeda), end='')
op2 = int(input(' para '))
if op2 == op1:
    print('\033[31mVocê ja esta convertendo essa moeda, tente outra.\033[m')
elif op1 == 1 and op2 == 2:
    dolar_euro = float(input('Quantos dólares quer converter? U$'))
    total = dolar_euro / dolar * euro
    print('U${} para Euro deu €{:.2f} Euros' .format(dolar_euro, total))
elif op1 == 1 and op2 == 3:
    dolar_libra = float(input('Quantos dólares quer converter? U$'))
    total = dolar_libra / dolar * libra
    print('U${} para Libra deu £{:.2f} Libras' .format(dolar_libra, total))
elif op1 == 1 and op2 == 4:
    dolar_reais = float(input('Quantos dólares quer converter? U$'))
    total = dolar_reais / dolar * reais
    print('U${} para Reais deu R${:.2f} Reais' .format(dolar_reais, total))
elif op1 == 2 and op2 == 1:
    euro_dolar = float(input('Quantos euros quer converter? €'))
    total = euro_dolar / euro * dolar
    print('€{} para Dólares deu U${:.2f} Dólares' .format(euro_dolar, total))
elif op1 == 2 and op2 == 3:
    euro_libra = float(input('Quantos euros quer converter? €'))
    total = euro_libra / euro * libra
    print('€{} para Libra deu £{:.2f} Libra' .format(euro_libra, total))
elif op1 == 2 and op2 == 4:
    euro_reais = float(input('Quantos euros quer converter? €'))
    total = euro_reais / euro * reais
    print('€{} para Reais deu R${:.2f} Reais' .format(euro_reais, total))
elif op1 == 3 and op2 == 1:
    libra_dolar = float(input('Quantas Libras quer converter? £'))
    total = libra_dolar / libra * dolar
    print('£{} para Dólar deu U${:.2f} Dólares' .format(libra_dolar, total))
elif op1 ==  3 and op2 == 2:
    libra_euro = float(input('Quantas Libras quer converter? £'))
    total = libra_euro / libra * euro
    print('£{} para Euro deu €{:.2f} Euros' .format(libra_euro, total))
elif op1 == 3 and op2 == 4:
    libra_reais = float(input('Quantas Libras quer converter? £'))
    total = libra_reais / libra * reais
    print('£{} para Reais deu R${} Reais')
elif op1 == 4 and op2 == 1:
    reais_dolar = float(input('Quantos Reais quer converter? R$'))
    total = reais_dolar / reais * dolar
    print('R${} para Dólares deu U${} Dólares')
elif op1 == 4 and op2 == 2:
    reais_euros = float(input('Quantos Reais quer converter? R$'))
    total = reais_euros / reais * euro
    print('R${} para Euros deu €{} Euros')
elif op1 == 4 and op2 == 3:
    reais_libra = float(input('Quantos Reais quer converter? R$'))
    total = reais_libra / reais * libra
    print('R${} para Libras deu £{} Libras')
print('\033[1;32mOBRIGADO POR USAR NOSSO MINI CONVERSOR\033[m')

# SE VOCÊ ESTA VENDO ESSE CODIGO NO MEU REPOSITORIO VAI UMA OBSERVAÇÃO: ESSA E A FORMA MAIS COMPLEXA DE FAZER UM CONVERSOR EXISTEM FORMAS MAIS PRATICAS COM BIBLIOTECA E SEM BIBLIOTECA