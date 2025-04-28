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
        print('A soma de {} + {} = {}'.format(a,b,a+b))
        break