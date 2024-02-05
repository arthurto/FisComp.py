# Em Python podemos escrever uma função para 
# realizar tarefas repetitivas para nós  
# digamos que queremos calcular o valor da 
# hipotenusa de um triângulo retângulo 
# dados dois lados, l1 e l2. 
from math import sqrt

def hipotenusa(l1,l2): 
    # A hipotenusa ao quadrado é igual à soma
    # dos quadrados dos catetos
    #
    # A raiz quadrada da soma dos quadrados
    # a sqrt() é uma função que calcula a raiz quadrada 
    # do que está entre os parênteses 
    # e quando um número, x, é elevado ao quadrado, precisamos 
    # escrever x**2. 
    # por exemplo, 2 ao quadrado é escrito como 2**2, que é igual a 4.
    return sqrt(l1**2 + l2**2) 

if __name__ == "__main__":
    print("Para um triângulo retângulo com lados 3 e 4 a hipotenusa é igual à:")
    print(hipotenusa(3,4))
