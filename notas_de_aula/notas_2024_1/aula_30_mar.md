# Dia 26 de Março de 2024 

Na aula do dia 26 de março nós falamos sobre estruturas de fluxo e operadores lógicos. 

A lógica Booleana é a lógica utilizada pelas linguagens de programação para operar diferentes valores de `Verdadeiro` ou `Falso` para o programa realizar diferentes tarefas dependendo das condições que se apresentam durante a sua execução.

Em programação é comum nos depararmos com situações diversas ao resolver um problema através de um algoritmo. 
Em determinadas situações algumas condições aparecem e precisamos preparar o programa para realizar diferentes procedimentos em diferentes situações. 
Uma das formas de fazer isso é utilizando estruturas de fluxo, as estruturas de fluxo guiam o programa, que utiliza operadores lógicos para decidir o que fazer em determinadas condiões. 
Um exemplo de uma condição variável pode ser encontrada no programa que calcula as soluções da equação de segundo grau, ou simplesmente o [programa que "faz a Baskara"](https://github.com/arthurto/FisComp.py/blob/main/notas_de_aula/notas_2024_1/codigos_alunos/daniel_21_03_2024_baskara.py).

O programa é esse: 
```python
import math

a = float(input("Digite o valor a: "))
b = float(input("Digite o valor b: "))
c = float(input("Digite o valor c: "))

x = ((-b + math.sqrt(math.pow(b,2.0)-4.0*a*c))/(2*a))
xx = ((-b - math.sqrt(math.pow(b,2.0)-4.0*a*c))/(2*a))

print("A primeira raiz é : "+"{:10.4f}".format(x))
print("A segunda raiz é : "+"{:10.4f}".format(xx))
```

Nele temos um problema, quando os valores que formam o $\Delta = b^2-4 ac$ for negativo, ou seja $\Delta < 0$(Delta menor que zero) a solução que envolve calcular uma raiz quadrada não funciona. Pois a função `sqrt()` do módulo `math` não funciona para argumentos negativos.

Para evitar uma mensagem de erro a gente poderia adicionar uma condição.

Como a seguinte 

```python
# Cria uma variável Delta
Delta = b**2 - 4*a*c

if Delta > 0.0:
    
    print("A primeira raiz é : "+"{:10.4f}".format(x))
    print("A segunda raiz é : "+"{:10.4f}".format(xx))
else:
    
    print("Delta é negativo, o resultado é imaginário/complexo.")
```

Aqui foi utilizada uma estrutura de controle de fluxo. O programa vai executar uma das duas possibilidades. Ele decide qual vai ser executada fazendo a verificação do valor da operação `Delta > 0.0`. 

Em python uma expressão como `1 > 0` tem como resultado um valor lógico, verdadeiro:`True` ou falso:`False`.
A expressão `if Delta > 0.0:` executa os comandos que estão na linha abaixo que estão "dentro do parágrafo", portanto nesse caso as funções `print()`. Note que elas estão a alguns espaços do início da linha, é isso que eu quero dizendo quando disse "dentro do parênteses", a identação do python é utilizada para delimitar diferentes "blocos" nos quais diferentes pedaços do programa estão organizados. Nesse caso temos dois blocos, o bloco inicial que está logo abaixo do `if` e o segundo bloco que está abaixo do `else`.
A expressão `if tal_coisa:` vai executar o bloco logo abaixo dela se a variável `tal_coisa` tiver valor `True`. 
Se `tal_coisa` tiver o valor `False` o bloco que será executado vai ser o bloco que está logo abaixo do `else`. 
Basicamente podemos entender o `if` e `else` como "se" e "senão". 

> "Se" tal coisa for verdade, faça isso, se não, faça essa outra coisa. 

### Exercício

Utilize um interpretador de python qualquer para verificas os valores de diferentes expressões lógicas.

- `1 > 0`
- `0 > 1`
- `1 == 2`
- `1 == 0`


## Operadores lógicos 

Diferentes condições que podemos expressar em forma de `True` ou `False` (Booleanos) podem interagir de diversas formas. Por isso utilizamos operadores lógicos entre diferentes condições. 
Usando operadores como `and` ou `or` são operadores lógicos que têm como entrada um valor Booleano e retornam outro valor Booleano. 

Outro operadores, como `==`, `!=`, `>`,`<`, são operadores de comparação, onde diferentes valores podem ser comparados e podemos obter diferentes resultados Booleanos.

Por exemplo, podemos comparar dois valores de string `"abrir"=="abrir"`. O resultado dessa expresssão vai ser um Booleano `True`.
Podemos comparar valores numéricos, por exemplo `0 > 1`, que vai retornar um valor `False`. 

### Exercício 

Continue testando diferentes operadores de comparação entre valores em algum interpretador de python da sua escolha.


