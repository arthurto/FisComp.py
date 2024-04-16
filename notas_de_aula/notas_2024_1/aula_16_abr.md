# Aula do dia 16 de Abril de 2024 

Assunto: Derivada numérica com o método da reta secante, ou diferenças finitas. 


A interpretação geométrica da derivada é de que o valor da derivada de uma função em um determinado ponto é igual ao coeficiente angular da reta tangente à curva da função naquele ponto.
Uma forma de obter um valor próximo da derivada de uma função em um ponto é utilizando o método da secante. 
Se uma reta tangente à um ponto é uma reta que "encosta" em apenas um ponto da curva, a reta secante é a reta que "corta" a curva em dois pontos distintos. 
O coeficiente angular de uma reta secante pode ser obtido simplesmente tomando a diferença finita entre a variação vertical, em $y$, e a variação horizontal, em $x$, desses dois pontos.

Digamos que queremos calcular o valor do coeficiente angular da reta secante à curva da função $f(x) = x^2 - 4$. 
Para isso vamos precisar de dois pontos que estão sob essa curva, um deles pode ser o ponto $(x_0,f(x_0))$. O outro pode ser o ponto $(x_0 + h, f(x_0 + h))$. 

A razão entre a diferença vertical e a horizontal pode ser escrita como:

$$ \frac{f(x_0 + h) - f(x_0)}{(x_0 + h) - x_0} = \frac{f(x_0 + h) - f(x_0)}{h}.$$

A definição de derivada por limites é muito similar à expressão anterior, na verdade a definição de derivada é igual à expressão anterior acrescida de um limite:

$$ \frac{df}{dx} = \lim_{h \rightarrow 0 } \frac{f(x+h) - f(x)}{h}.$$

Tomando o limite de $h$ indo a zero nós obtemos a definição da derivada. 
Portanto, para um $h$ suficientemente pequeno, porém não nulo, é possível obter uma aproximação da derivada no ponto $x_0$. 


O nome desse método para aproximação numérica da derivada da função $f(x)$ é chamado de "método das diferenças finitas".
Nesse caso é uma derivada progressiva, pois temos $f(x+h)$, existe também a regressiva e a central, que não cabem no escopo atual, mas existem e merecem ser mencionadas. 



## Demonstrando a derivada de $x^2 -4$ no ponto $x = 2$. 

A derivada exata da função $f(x) = x^2 -4$ é igual a $\frac{d f }{dx} =f'(x) = 2x$. 
Portanto o valor da derivada de $f(x)$ quando $x = 2$ vai ser igual a $f'(2)=4$. 


Vamos escrever um programa em python que demonstre que o valor da derivada numérica se aproxima ao valor exato da derivada em $x=2$ para consecutivos $h$ menores. 

Para isso vamos escrever uma função em python que retorne o valor da função $f(x)$, em seguida uma outra função que nos retorna a derivada numérica de $f(x)$ no ponto $x$ para um tamanho arbitrário de $h$. 

```python 
# 
# Definido a função que vai ser derivada 
# 
def f(x): # a função f(x) tem como argumento o número x. 
    # ** é a forma de escrever potência em python
    return x**2 - 4  

# 
# Definindo a função que deriva uma função f qualquer, em um ponto x, com um passo h. 
# 
def num_deriv(f,x,h):
    return (f(x+h) - f(x))/h


# Agora vamos escrever 
# um loop que vai passar por diferentes valores de h 
# criando um vetor com os valores de h que eu quero testar 
varios_hs = [1,0.5,0.1,0.01,0.001,0.0001,0.00000001]

x_0 = 2

for h in varios_hs:
    dfdx = num_deriv(f,x_0,h)
    print(f"A derivada da função f(x)\n em x = {x_0}\n com passo h = {h}\n é dfdx = {dfdx}")
```

O resultado desse script quando executado deve ser algo como: 
```bash 
A derivada da função f(x)
 em x = 2
 com passo h = 1
 é dfdx = 5.0
A derivada da função f(x)
 em x = 2
 com passo h = 0.5
 é dfdx = 4.5
A derivada da função f(x)
 em x = 2
 com passo h = 0.1
 é dfdx = 4.100000000000001
A derivada da função f(x)
 em x = 2
 com passo h = 0.01
 é dfdx = 4.009999999999891
A derivada da função f(x)
 em x = 2
 com passo h = 0.001
 é dfdx = 4.000999999999699
A derivada da função f(x)
 em x = 2
 com passo h = 0.0001
 é dfdx = 4.0001000000078335
A derivada da função f(x)
 em x = 2
 com passo h = 1e-08
 é dfdx = 3.999999975690116
```

