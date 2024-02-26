print('Digite sua idade: ')
idade = int(input())

print('No ano que vem a sua idade será', idade+ 1)

if idade <= 12:
    print('Você é uma criança')

elif idade < 18:
    print('Você é um adolescente')

elif idade < 60:
    print('Você é um adulto')

else:
    print('Você é um idoso')