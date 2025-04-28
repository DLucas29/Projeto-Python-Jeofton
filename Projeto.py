print('Adição do arquivo principal')
c = 0
while c != 0:
    print('''[1] Realizar soma
          [2] Realizar subtração
          [3] Realizar Multiplicação
          [4] Fechar o Programa''')
    c = int(input('Opção: '))
    if c == 1:
        a = int(input('Primeiro valor: '))
        b = int(input('Segundo valor: '))
        print('A soma de {} + {} = {}'.format(a, b, a+b))
        break
    elif c == 2:
        a = int(input('Primeiro valor: '))
        b = int(input('Segundo valor: '))
        if a > b:
            print('A subtração de {} - {} = {}'.format(a, b, a-b))
        else:
            print('A subtração de {} - {} = {}'.format(b, a, b-a))
        break
    elif c == 3:
        a = int(input('Primeiro valor: '))
        b = int(input('Segundo valor: '))
        print('A multiplicação de {} * {} = {}'.format(a, b, a*b))
        break
print('\033[31mFim do programa.\033[m.')
