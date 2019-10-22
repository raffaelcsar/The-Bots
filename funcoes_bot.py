def novo_pedido():
    """Realiza todo o tratamento de um novo pedido"""

    global tamanho
    
    #Tratamento de decisoes no pedido
    while(True):
        print('Qual o tamanho da sua pizza?\n'
                '1.  PEQUENA\n'
                '2.  MÉDIA\n'
                '3.  GRANDE')

        option = input()
        if option.isnumeric():
            option = int(option)
            if option == 1:
                return um_sabor(option)

            elif option == 2:
                opt_sabor = input('Deseja sua pizza com quantos sabores?\n(1) 1 Sabor\n(2) 2 Sabores\n')
                if opt_sabor == 1:
                    return um_sabor(option)
                else:
                    return dois_sabores(option)

            elif option == 3:
                opt_sabor = input('Deseja sua pizza com quantos sabores?\n'
                                    '(1) 1 Sabor\n'
                                    '(2) 2 Sabores\n'
                                    '(3) 3 Sabores\n')
                if option == 1:
                    return um_sabor(option)
                elif option == 2:
                    return dois_sabores(option)
                elif option == 3:
                    return tres_sabores()
        elif option.isalpha():
            option = option.upper()
            if option == 'PEQUENA':
                return um_sabor(option)

            elif option == 'MEDIA':
                opt_sabor = input('Deseja sua pizza com quantos sabores?\n(1) 1 Sabor\n(2) 2 Sabores\n')
                if opt_sabor == 1:
                    return um_sabor(option)
                else:
                    return dois_sabores(option)

            elif option == 'GRANDE':
                opt_sabor = input('Deseja sua pizza com quantos sabores?\n'
                                    '(1) 1 Sabor\n'
                                    '(2) 2 Sabores\n'
                                    '(3) 3 Sabores\n')    

       

def show_cardapio():
        """Mostra o cardapio do estabelecimento, arquivado em um .txt"""
        cardapio = open('cardapio.txt', 'r')
        for item in cardapio:
            print(item)
        cardapio.close() 
def um_sabor(option):
        """Escolha do sabor para apenas um sabor"""

        global tamanho

        if option == 1 or option == 'PEQUENA':
            tamanho = 'Pequena'
        elif option == 2 or option == 'MEDIA':
            tamanho = 'Media'
        elif option == 3 or option == 'GRANDE':
            tamanho = 'Grande'
        show_cardapio()
        while (True):
            sabor = input('Insira o numero referente ao sabor desejado:\n')
            if sabor.isnumeric():
                more_options()
            else:
                print('Ops! Digite apenas o número referente ao sabor:\n')
    
def dois_sabores(option):
    """Escolha do sabor para duas opcoes"""

    global tamanho

    if option == 2:
        tamanho = 'Media'
    elif option == 3:
        tamanho = 'Grande'
        
    sabores = []
    while (True):
        show_cardapio()
        sabor_1 = input('Insira o numero referente ao primeiro sabor desejado:\n')
        #Validando se o valor do sabor_1 eh um numero para poder ser adicionado ao pedido
        if sabor_1.isnumeric():
            sabores.append(sabor_1)
            sabor_2 = input('Insira o numero referente ao segundo sabor desejado:\n')
            #Validando se o valor do sabor_2 eh um numero para poder adicionar ao pedido
            if sabor_2.isnumeric():
                sabores.append(sabor_2)
                break
            else:
                print('Ops! Digite apenas o número referente ao sabor:\n')
        else:
            print('Ops! Digite apenas o número referente ao sabor:\n')
        #Condicao de parada do loop
        if len(sabores) == 2:
            more_options()
            return sabores
            break

def tres_sabores():
    """Escolha dos sabores para tres opcoes"""

    global tamanho
    tamanho = 'Grande'
    sabores = []
    show_cardapio()
    while (True):
        sabor_1 = input('Insira o numero referente ao primeiro sabor desejado:\n')
        #Validando se o valor do sabor_1 eh um numero para poder ser adicionado ao pedido
        if sabor_1.isnumeric():
            sabores.append(sabor_1)
            break
        else:
            print('Ops! Digite apenas o número referente ao sabor:\n')
    while (True):
        sabor_2 = input('Insira o numero referente ao segundo sabor desejado:\n')
        # Validando se o valor do sabor_1 eh um numero para poder ser adicionado ao pedido
        if sabor_2.isnumeric():
            sabores.append(sabor_2)
            break
        else:
            print('Ops! Digite apenas o número referente ao sabor:\n')
    while (True):
        sabor_3 = input('Insira o numero referente ao terceiro sabor desejado:\n')
        # Validando se o valor do sabor_1 eh um numero para poder ser adicionado ao pedido
        if sabor_3.isnumeric():
            sabores.append(sabor_3)
            break
        else:
            print('Ops! Digite apenas o número referente ao sabor:\n')


def more_options():
    borders = ['Catupiry', 'Cheddar', 'Calabresa', 'Queijo', 'Nutela']
    refrigerante = ['Coca-cola', 'Fanta', 'Sprite', 'Kuat', 'Guaraná Antartica']
    
    opt_border = int(input('Deseja adicionar borda?\n(1) SIM\n(2) NÃO'))
    if opt_border == 1:
        print('Escolha o recheio da borda:')
        for i in range(len(borders)):
            print(i,borders[i])
        add_border = int(input())
    more_add = int(input('Deseja adicionar alguma bebida ao seu pedido?\n(1) SIM\n(2) NÃO'))
    if more_add == 1:
        print('Escolha o seu refrigerante:')
        for i in range(len(refrigerante)):
            print(i, refrigerante[i])
        add_refri = int(input())
    return(total_pedido)
    

'''def total_pedido(total):
    print('Por favor, confirme seu pedido:')
    for i in total:
        print(i)
    answer = int(input('O seu pedido está correto?\n(1) SIM\n(2) NÃO'))
    if answer == 1:
        return(payment)
    else:
        return(alteracao_pedido)'''

def payment():

    opt_payment = int(input('Qual a forma de pagamento:\n(1) Dinheiro\n(2) Cartão'))
    if opt_payment == 1:
        pay_back = input('Deseja troco?\n(1) SIM\n(2) NÃO')
        if pay_back == 1:
            print('Para quanto deseja o troco?')
            client_money = int(input())
            return(client_money - total_pedido)
    else:
        print('O motoboy levará a máquineta para o pagamento no ato da entrega!')
        print('Agradecemos sua preferência!')


tamanho = ''
novo_pedido()