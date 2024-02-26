#Estrutura de repetição
'''Utilizado para repetir uma instrução determinado número de vezes'''

for x in range(1,5):
    nome = input('Digite o nome do aluno: ')
    nota = int(input('Digite a nota do aluno: '))
    if nota >=6:
        print(f"{nome} foi aprovado, com a nota", nota)
    else:
        print (f"{nome} foi reprovado, com a nota {nota: .2f}") 
    
    #esse .2f é de float,
    #o número antes e depois  do ponto, definem o número de casas que vai vir antes e depois da vírugla, 
    #já o primeiro é de format, e é necessário para mostrar as variáveis dentro de chave.