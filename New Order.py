def novo_pedido():
    cardapio = ('NOSSAS OPÇÕES DE SABORES\n\n'
                '1. AMERICANA\n'
                'MOLHO DE TOMATE, MUSSARELA, BACON, CALABRESA, OVOS E CEBOLA\n'
                '2. APRESUNTADA\n'
                'MOLHO DE TOMATE, PRESUNTO E MUSSARELA\n'
                '3. CROCANTE\n'
                'MOLHO DE TOMATE, MUSSARELA (2 CAMADAS), CATUPIRY, BATATA PALHA (DEPOIS DE ASSADA)\n'
                '4. MILHO\n'
                'MOLHO DE TOMATE, MUSSARELA E MILHO\n'
                '5. MUSSARELA\n'
                'MOLHO DE TOMATE E MUSSARELA (2 CAMADAS)\n'
                '6. TRADICIONAL\n'
                'MOLHO DE TOMATE, PRESUNTO, TOMATES E MUSSARELA\n'
                '7. ALHO E ÓLEO\n'
                'MOLHO DE TOMATE, MUSSARELA, ALHO E AZEITE DE OLIVA\n'
                '8. BACON\n'
                'MOLHO DE TOMATE, MUSSARELA E BACON\n'
                '9. CALABRESA\n'
                'MOLHO DE TOMATE, MUSSARELA E CALABRESA\n'
                '10. ESCAROLA\n'
                'MOLHO DE TOMATE, ESCAROLA (REFOGADA), BACON, ALHO (OPCIONAL) E MUSSARELA\n'
                '11. FRANGO\n'
                'MOLHO DE TOMATE, MUSSARELA, FRANGO DESFIADO E REFOGADO\n'
                '12. FRANGO C/ CATUPIRY\n'
                'MOLHO DE TOMATE, MUSSARELA, FRANGO DESFIADO AO MOLHO DE CATUPIRY\n'
                '13. FRAN-MILHO\n'
                'MOLHO DE TOMATE, MUSSARELA, FRANGO DESFIADO AO MOLHO E MILHO\n'
                '14. MARGUERITA\n'
                'MOLHO DE TOMATE, TOMATES, PARMESÃO, MANJERICÃO, AZEITE DE OLIVA E MUSSARELA\n'
                '15. MEXICANA\n'
                'MOLHO DE TOMATE, MUSSARELA, CALABRESA RALADA, PIMENTÃO VERDE E PIMENTA-CALABRESA\n'
                '16. NAPOLITANA\n'
                'MOLHO DE TOMATE, TOMATES, PROVOLONE E MUSSARELA\n'
                '17. PAULISTA\n'
                'MOLHO DE TOMATE, MUSSARELA, MILHO, ERVILHA, PALMITO E AZEITONAS\n'
                '18. PORTUGUESA\n'
                'MOLHO DE TOMATE, PRESUNTO, MUSSARELA, OVOS, CEBOLA E AZEITONAS\n'
                '19. TOSCANA\n'
                'MOLHO DE TOMATE, MUSSARELA, CALABRESA E OVOS\n'
                '20. ALICHE\n'
                'MOLHO DE TOMATE, MUSSARELA, ALICHE E TOMATES\n')
    numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20')
    global tamanho
    while(True):
        print('Qual o tamanho da sua pizza?\n'
              '1.  PEQUENA\n'
              '2.  MÉDIA\n'
              '3.  GRANDE')
        option = (input())
        options = ('1','2','3')
        #OPTION 1 - SMALL
        if option in options and option == '1':
            tamanho = 'PEQUENA'
            print(cardapio)
            #SABOR - JUST ONE
            while(True):
                sabores.insert(0, input('Qual o sabor?'))
                if sabores[0] in numbers:
                    break
                else:
                    print('Opção invalida, tente novamente!\nATENÇÃO! Digite apenas o número referente ao que desejar.\n')
                    sabores.pop(0)

            break
        #OPTION 2 - MEDIUM
        elif option in options and option == '2':
            tamanho = 'MÉDIA'
            print(cardapio)
            while(True):
                sabor = (input('Quantos sabores deseja:\n1. Um sabor\n2. Dois sabores'))
                sabor_1 = ('1', '2')
                #SABOR 1 - JUST ONE
                if sabor in sabor_1 and sabor == '1':
                    while(True):
                        sabores.insert(0, input('Insira o sabor.'))
                        if sabores[0] in numbers:
                            break
                        else:
                            print('Opção invalida, tente novamente!\nATENÇÃO! Digite apenas o número referente ao que desejar.\n')
                            sabores.pop(0)
                    break
                #SABOR 2 - TWO CHOICES
                elif sabor in sabor_1 and sabor == '2':
                #FIRST CHOICE
                    while(True):
                        sabores.insert(0, input('Insira o primeiro sabor.'))
                        if sabores[0] in numbers:
                            break
                        else:
                            print('Opção invalida, tente novamente!\nATENÇÃO! Digite apenas o número referente ao que desejar.\n')
                            sabores.pop(0)
                #SEGUND CHOICE
                    while(True):
                        sabores.insert(1, input('Insira o segundo sabor.'))
                        if sabores[1] in numbers:
                            break
                        else:
                            print('Opção invalida, tente novamente!\nATENÇÃO! Digite apenas o número referente ao que desejar.\n')
                        sabores.pop(1)
                    break
                else:
                    print('Opção invalida, tente novamente!\nATENÇÃO! Digite apenas o número referente ao que desejar.\n')

            break
        #OPTION 3 - LARGE
        elif option in options and option == '3':
            tamanho = 'GRANDE'
            print(cardapio)
            while(True):
                sabor = (input('Quantos sabores deseja:\n1. Um sabor\n2. Dois sabores\n3. Três sabores'))
                sabor_1 = ('1', '2', '3')
            #JUST ONE
                if sabor in sabor_1 and sabor == '1':
                    while (True):
                        sabores.insert(0, input('Insira o sabor.'))
                        if sabores[0] in numbers:
                            break
                        else:
                            print('Opção invalida, tente novamente!\nATENÇÃO! Digite apenas o número referente ao que desejar.\n')
                            sabores.pop(0)
                    break
            #TWO CHOICES
                elif sabor in sabor_1 and sabor == '2':
                #FIRST CHOICE
                    while (True):
                        sabores.insert(0, input('Insira o primeiro sabor.'))
                        if sabores[0] in numbers:
                            break
                        else:
                            print('Opção invalida, tente novamente!\nATENÇÃO! Digite apenas o número referente ao que desejar.\n')
                            sabores.pop(0)
                #SECOND CHOICE
                    while (True):
                        sabores.insert(1, input('Insira o segundo sabor.'))
                        if sabores[1] in numbers:
                            break
                        else:
                            print('Opção invalida, tente novamente!\nATENÇÃO! Digite apenas o número referente ao que desejar.\n')
                            sabores.pop(1)
                    break
                elif sabor in sabor_1 and sabor == '3':
                #THIRD CHOICE
                    while(True):
                        sabores.insert(0, input('Insira o primeiro sabor.'))
                        if sabores[0] in numbers:
                            break
                        else:
                            print('Opção invalida, tente novamente!\nATENÇÃO! Digite apenas o número referente ao que desejar.\n')
                            sabores.pop(0)
                    while(True):
                        sabores.insert(1, input('Insira o segundo sabor.'))
                        if sabores[1] in numbers:
                            break
                        else:
                            print('Opção invalida, tente novamente!\nATENÇÃO! Digite apenas o número referente ao que desejar.\n')
                            sabores.pop(1)
                    while(True):
                        sabores.insert(2, input('Insira o terceiro sabor.'))
                        if sabores[2] in numbers:
                            break
                        else:
                            print('Opção invalida, tente novamente!\nATENÇÃO! Digite apenas o número referente ao que desejar.\n')
                            sabores.pop(2)
                    break
                else:
                    print('Opção invalida, tente novamente!\nATENÇÃO! Digite apenas o número referente ao que desejar.\n')
            break
        else:
            print('Opção invalida, tente novamente!\n'
                  'ATENÇÃO! Digite apenas o número referente ao que desejar.\n')
def printout():
    for i in range(0, len(sabores)):
        escolhas.append(list(map(int, sabores[i].split())))
        for x in escolhas[i]:
            print(menu[x], end=', ')

menu = {
    1:"AMERICANA",
    2:"APRESUNTADA",
    3:"CROCANTE",
    4:"MILHO",
    5:"MUSSARELA",
    6:"TRADICIONAL",
    7:"ALHO E ÓLEO",
    8:"BACON",
    9:"CALABRESA",
    10:"ESCAROLA",
    11:"FRANGO",
    12:"FRANGO C/ CATUPIRY",
    13:"FRAN-MILHO",
    14:"MARGUERITA",
    15:"MEXICANA",
    16:"NAPOLITANA",
    17:"PAULISTA",
    18:"PORTUGUESA",
    19:"TOSCANA",
    20:"ALICHE"
}


tamanho = ''
sabores = []
escolhas = []
novo_pedido()
print('\nVocê escolheu a pizza de tamanho {}\nNos sabores de: '.format(tamanho))
printout()
print('Confirma o pedido?')