num = int(input('Digite um numero: '))
print('''Escolha uma das bases para a conversão: 
[ 1 ] converter para Binário
[ 2 ] converter para Octal
[ 3 ] converter para Hexadecimal''')
esc = int(input('Sua opção: '))
if esc == 1:
    print('A conversão de {} para Binário é {}' .format(num, bin(num)[2:]))
elif esc == 2:
    print('A conversão de {} para Octal é {}' .format(num, oct(num)[2:]))
elif esc == 3:
    print('A conversão de {} para Hexadecimal é {}' .format(num, hex(num)[2:]))
else:
    print('\033[1;31mOpção invalida, tente novamente!\033[m')