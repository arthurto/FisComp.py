# Aula do dia 11 de Abril de 2024

Nessa aula nós continuamos as atividades da aula anterior. 
Os nossos objetivos eram criar 3 programas com objetivos diferentes. 
O primeiro seria um programa que contém apenas a definição de uma função que vai ser chamada mais tarde.
O segundo seria um programa para criar um arquivo com os dados e o terceiro seria um programa para utilizar as funções criadas nos outros dois programas para criar um arquivo com duas colunas, $x$ e $y$.


Nessa aula nós nos aprofundamos sobre a função `open` da biblioteca base do python. 
Com ela podemos criar, abrir, ler e escrever conteúdos em documentos no computador.


Um exemplo de uso da função `open` é o seguinte: 
```python
arquivo = open('nome.txt','w')

arquivo.write("Olá arquivo")

arquivo.close()
```

O que esse pedaço de código faz é criar um arquivo chamado `'nome.txt'`, escrever nele a mensagem `"Olá arquivo"` e depois fechar o objeto arquivo. 


Na primeira linha desse código temos um atribuição à variável `arquivo`. 
À variável `arquivo` é atribuída um objeto arquivo do python, que é o "output" da função `open()`. 
Os argumentos da função `open('nome.txt','w')` são, em ordem, o nome do arquivo e o método de escrita ou leitura que será aplicado. 

 - O método `'w'` significa 'escrever' ou 'write', em inglês. Com esse método nós escrevemos um arquivo inteiro do início. Criando um arquivo novo ou reescrevento totalmente um arquivo já existente. 
 - O método `'w+'` serve para escrever e ler um arquivo, as mesmas regras anteriores se aplicam. Teste! 
 - O método `'r'` serve para ler o arquivo. 
 - O método `'a'` serve para escrever coisas no final do arquivo que já existe, se ele não existe é criado, mas se existe ele vai adicionar as próximas entradas no final do arquivo. 


Agora vocês podem construir uma função que tenha como entrada 3 argumentos: 
 - `nome`: uma string com o nome do arquivo que tu deseja criar. 
 - `x`: um array de números inteiros ou floats que vão representar os valores de $x$ de um gráfico. 
 - `y`: um arrat de números inteiros ou floats que vão representar os valores de $y$ de um gráfico. 

 A função deve ser escrita com a seguinte estrutura: 
```python 
def escreve_arquivo(nome,x,y):
    # lógica da função
    # aqui vocês vão desenvolver o programa
    pass
```

Na aula anteiror a gente aprendeu sobre como chamar funções de diferentes arquivos para serem executadas em outras funções. 

