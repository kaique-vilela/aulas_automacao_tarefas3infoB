
while True:
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))
    op = input('Digite um operador matemático: ')
    if op == '+':
        print(f'{n1} + {n2} = {n1 + n2}')
    elif op == '-':
        print(f'{n1} - {n2} = {n1 - n2}')
    elif (op == '*') or (op =='x'):
        print(f'{n1} * {n2} = {n1 * n2}')
    elif op == '/':
        print(f'{n1} / {n2} = {n1 / n2}')
    else:
        print('Operador desconhecido!')
    
    resp = input('Você quer continuar? (sim ou não)')
    if resp == 'não':
        break

    
