n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
op = input('Digite um operador matemático: ')

if op == '+':
    print(f'{n1} + {n2} = {n1 + n2}')

elif op == '-':
    print(f'{n1} - {n2} = {n1 - n2}')

elif (op == '*') or (op =='x'):
    print(f'{n1} * {n2} = {n1 * n2}')

elif op == '/':
    print(f'{n1} / {n2} = {n1 / n2}')
