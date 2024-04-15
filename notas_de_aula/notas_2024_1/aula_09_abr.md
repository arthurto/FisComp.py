# Aula do dia 09 de Abril de 2024

Na aula de hoje foi lançado um desafio. 
Criar 3 arquivos. 
- Um chamado 'func.py' que vai conter uma função matemática qualquer para criar os pontos de um gráfico. 
- Um chamado 'cria_file.py' que vai conter uma função que cria um arquivo com duas colunas de pontos. 
- Um chamado 'main.py' que vai chamar indepentemente cada um deles e utilizar eles para criar o arquivo com os valores desejados. 

## Chamando funções de outros arquivos em python

Digamos que o arquivo `func.py` conténha o seguinte conteúdo: 


```python
import math 

def f(x):
    return math.exp(- x**2)*x
```

Agora digamos que outro arquivo, na mesma pasta, deseja chamar essa função $f(x)$ definida no arquivo `func.py`. 

Para isso o outro arquivo pode fazer da mesma forma como se faz para importar funções de uma biblioteca. 
Por exemplo: 

```python
import func 

# usando a função 
# para calcular o seu valor quando 
# x = 0.1 
print(func.f(0.1))
```

Dessa forma estamos chamando o arquivo inteiro `func.py`. 

Podemos chamar a mesma função de outra forma, chamando apenas a função `f`. 

```python
from func import f 

# usando novamente a função 
print(f(0.1))
```

Dessa vez chamamos apenas a função `f` em vez do arquivo inteiro. 



## Conteúdo bônus: 

Quando executamos um programa em python temos algumas diferenças entre chamar ele diretamente do terminal como `python3 func.py` por exemplo e entre chamar uma função que chama ele. 
Mais específicamente, existe uma variável interna chamada `__name__` que possui a string `__main__` se você a chama diretamente.

Utilizando esse fato, de variáveis internas do programa possuírem valores diferentes, podemos criar comportamentos específicos para programas que são feitos apenas para serem chamados por outros. 
Isso pode ser útil para uma enorme gama de possibilidades, como por exemplo, testar se o programa que criou realiza corretamente as tarefas que ele deveria fazer. Testar diferentes `edge-cases` ou `casos teste`. Dentre outras coisas. 

Para criar um comportamento desses é comum criar uma função `main()` e um condicional no final do arquivo. 

Por exemplo, caso a gente queira testar que o arquivo `func.py` esteja corretamente criando os valores para a função $f(x) = x e^{-x^2}$, podemos reescrever ele da seguinte maneira: 

```python 
import math

def f(x):
    return math.exp(-(x**2))*x 

# uma função para testar o valor da função 
# f(x) quando x = 2 
# e printar o valor na tela 

def main(): # função sem argumento, ela só vai exeutar o que estiver dentro dela
    # eu quero testar alguns valores de x e^(-x^2)
    print('x e^(-x^2) quando x = 2')
    print(f(2))
    print('\n') # Quebra de linha


# Se a variável __name__ tiver o valor "__main__"
# execute a função main(). 
if __name__ == "__main__":
    main()
```

