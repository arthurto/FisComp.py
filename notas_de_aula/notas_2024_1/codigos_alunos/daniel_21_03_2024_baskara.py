# Esse código foi desenvolvido pelo aluno Daniel 
# durante uma aula de computação básica para física 
# no dia 21/03/2024

import math

a = float(input("Digite o valor a: "))
b = float(input("Digite o valor b: "))
c = float(input("Digite o valor c: "))

x = ((-b + math.sqrt(math.pow(b,2.0)-4.0*a*c))/(2*a))
xx = ((-b - math.sqrt(math.pow(b,2.0)-4.0*a*c))/(2*a))

print("A primeira raiz é : "+"{:10.4f}".format(x))
print("A segunda raiz é : "+"{:10.4f}".format(xx))
