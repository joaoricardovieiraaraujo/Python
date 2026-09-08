print('Informe as seguintes informações')
produto = str(input('Nome do produto: '))
quantidade = int(input('Quantidade em estoque: '))
preco = float(input('Preço do produto: '))
venda = int(input('Quantidade vendida: '))
if venda > quantidade:
    print('\033[31mNão é possível vender mais do que o estoque disponível.\033[m')
elif venda <= quantidade:
    quantidade -= venda
    venda_total = venda * preco
    print('\033[32mVenda realizada com sucesso!\033[m agora no estoque temos {} e o valor total da venda foi de \033[33mR${:.2f}\033[3' .format(quantidade, venda_total))
