# Notas de aula do dia 21 de Março de 2024 

## Sintaxe 

A sintaxe de uma linguagem é a forma como escrevemos. 
A sintaxe se preocupa como os elementos de uma frase, ou de uma linha de código, é escrita. 
Nas linguagens de programação a sintaxe possui regras que são seguidas pelo interpretador ou pelo compilador para executar o programa da forma como ele foi __escrito__. 
A forma como o programa é __escrito__ é como ele vai ser executado, nem sempre ele vai ser executado da forma desejada, isso ocorre quando a sintaxe não está correta, ou está correta (não possui erros) mas possui um comportamento diferente do que gostaríamos.

Um bom entendimendo da sintaxe é necessário para entedermos como um programa funciona e como podemos "traduzir" as nossas ideias, ou os algoritmos que queremos executar, para um programa fazer o que queremos que ele faça. 

### Comentários 

Em linguagens de programação é comum que se tenha diferentes formas de escrever comentários nos códigos. 
Os comentários são ignorados pelo compilador ou interpretador da linguagem e servem apenas para fazer anotações no programa. 
Eles podem ter diferentes funcionalidades, como explicar o que cada linha do programa faz ou para servir de guia para próximas pessoas que forem utilizar os programas caso eles precisem de alterações. 
É muito importante escrever comentários relevantes que possam ajudar pessoas no futuro a entender os seus programas, muitas vezes essa pessoa do futuro pode ser __você__.

## Variável 

Variáveis são símbolos que guardam informação. É comum escrevermos programas que funcionem para calcular quantidades, por exemplo, ou para trocar mensagens. 
Quais são essas quantidades ou quais são essas mensagens nós não sabemos, essas coisas vão mudar toda vez que o programa for executado. 
Mesmo assim a lógica do que fazemos com essas quantidades vai ser sempre a mesma, então podemos escrever um programa que funcionaria para qualquer valor.

A operação de "pegar" um valor e "guardar" ou "escrever" ele em um símbolo é chamado de atribuição.
Em python o operador de atribuição é o símbolo `=`, que não pode ser utilizado para guardar informação nenhuma. Nenhum símbolo de operação pode ser utilizado para guardar outra informação. 

Então se quisermos guardar uma variável que é aproximadamente o número $\pi$ podemos fazer isso da seguinte maneira:
```
pi = 3.1415926
```
O que isso significa é que na variável chamada `pi` está guardado o número do tipo "float" que é igual a `3.1415926`.
Toda vez que essa variável `pi` aparecer em algum lugar, ela se comportará como o número que está guardado nela.

Essas ideias são muito poderosas e podem ser utilizadas para criar programas que realizam diferentes tarefas.

### Tipos 

Para podemos utilizar uma linguagem de programação para resolver problemas reais precisamos poder realizar operações entre quantidades, como números ou texto. 
A informação existe em diversos tipos, um número de telefone pode ser um número inteiro, mas pode ser melhor representado como um texto, devido aos outros caracteres, por exemplo.

> O que é mais fácil de ler? 
> `5555999991111` ou `"+55 (55) 99999 1111"`?

Dependendo do contexto a informação pode ser representada de diferentes formas, e os diferentes tipos são uma forma de classificar diferentes tipos de informação.


#### Tipos numéricos 

Nessa matéria vamos utilizar diferentes valores 

- float: "floating point number" ou "número com algarismo decimal" (ou "real"), é uma forma de representar números com diferentes casas depois da vírgula.  
- - Bom para cálculos numéricos que exigem precisão.
- - Escrevemos números float com `.` como separador decimal e não `,`. 
- - Por exemplo `0.1254` ou `3.1415926`. 

- int: "integer" ou "número inteiro", é uma forma de representar números inteiros, 
- - Bom para contagem ou coisas que tomam valores inteiros.
- - Escrevemos números inteiros sem `.`. 
- - Como por exemplo: `12` ou `1917`.

Diferentes operações entre tipos numéricos podem levar a resultados diferentes em diferentes linguagens, é importante testar elas antes de colocar em seu programa. 
Uma forma útil de fazer isso é utilizando a função `print()` com o valor dentro, mostrando o valor na tela.

Por exemplo, em python 2 temos como resulado da divisão entre dois números inteiros um número inteiro. 
Em python 3 o resultado pode ser tanto um inteiro como um float. Experimente! 

#### Tipo "string" ou "frase"

O tipo string é um tipo que pode ser tanto um caracter ou uma concatenação de caracteres. Nem todos os caracteres são suportados por todas as linguagens.
Em python 3 podemos utilizar praticamente todos os caracteres presentes no teclado. 

Variáveis do tipo string podem ser utilizadas para mostrar informações ou para guardar informações em formato de texto.

Uma string em python é definida como o conjunto de caracteres que é escrito entre aspas ('') ou aspas duplas (""). 

Por exemplo `"isso é uma string"` e `'isso também é uma string'`. 


