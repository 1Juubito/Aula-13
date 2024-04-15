print('Escolha o que deseja comprar')
print('1 - Maçã')
print('2 - Laranja')
print('3 - Banana')

produto = int(input('Qual sua escolha?'))
qtd = int(input('Quantas unidades?'))

if (produto == 1): #maçã
    pagar = qtd * 2.3
    print(f'Você comprou {qtd} maçãs. Total à pagar: {pagar}')
elif (produto == 2): #laranja
        pagar =qtd * 3.6
        print(f' Você comprou {qtd} laranjas. Total à pagar: {pagar}')
elif (produto == 3): #banana
            pagar = qtd * 1.85
            print(f'Você comprou {qtd} bananas. Total à pagar: {pagar}')
else:
            print('Produto inexistente')

            