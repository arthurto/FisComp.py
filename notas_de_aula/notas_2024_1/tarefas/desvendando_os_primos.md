# Desvendando a função de números primos 

Temos aqui uma função que nos diz se um número `n` é primo ou não. 

```python 
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
```

Essa função tem como entrada um número `n` e tem como saída um valor booleano de `True` ou `False`. 

A partir da sintaxe da função e das operações que ela executa, explique as seguintes perguntas. 

1 - Como funciona uma estrutura de controle de fluxo com `if`, `else` e `elif`? Escreva com suas próprias palavas como funciona cada uma dessas estruturas.


2 - Essa função possui diversas operações, são elas `<=`, `%`, `*`, `==`, `+=` e `or`. Escreva um pequeno texto explicando o funcionamento de cada uma delas, em quais tipos de variáveis elas atuam e qual é a saída das operações que elas realizam?


> Exemplo: O operador `and` em python é um operador lógico que realiza uma operação entre dois valores boolenos (`True` ou `False`):`bool1 and bool2`, que tem como saída outro valor booleano. 


3 - Imagine que você esteja ensinando uma outra pessoa a realizar a mesma tarefa que essa função em python está executando, imagine que você precisa entregar a essa pessoa uma folha de papel com as instruções, passo a passo, de como realizar a mesma tarefa que essa função realiza. Escreva esse texto.
