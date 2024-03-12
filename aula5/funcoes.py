''' As funções são utilizadas para modularizar o código, ou seja,
 dividi-lo em partes menores, que podem ser reutilizadas.
 
 Estrutura:

 def nome_funcao(param1,param2):
 faz algo
 return valor

 Exemplo:
 '''
#função 1
def calcularAreaTriangulo(base,altura):
    area = (base * altura) / 2
    return area

#função 2
def login(usuario1,senha):
    if usuario1 == 'admin' and senha == '123':
        return True
    else:
        return False
    
#chamando a função

#area = calcularAreaTriangulo(100,50)
#print(f'A area do triângulo é {area}')

#print(login('kaique','124')) //o resultado seria false

#print(login('admin','123')) //o resultado seria true



