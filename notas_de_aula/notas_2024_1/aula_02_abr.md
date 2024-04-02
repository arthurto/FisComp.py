# Aula do dia 02 de Abril de 2024 

Nessa aula a gente reviso alguns conceitos básicos de funções e como criar e popular vetores (Arrays) em python utilizando loops "while". 

Um loop while funciona como um loop de repetição qualquer, que vai executar o que estiver contido em seu interior (dentro do 'parágrafo') até que a condição fornecida seja falsa. A estrutura geral é a seguinte: 
```python 
while (condição):
	(código a ser repetido)
```

Podemo por exemplo utilizar o programa para popular um vetor vazio. 
Digamos que queremos preencher um vetor vazio com valores que começam em `0.0`até `100.0` com passo arbitrário. Podemos fazer isso da seguinte maneira: 
```python 
vetor = [] # define vetor vazio 
x0 = 0.0 # variável de início 
passo = 0.25 # define passo arbitrário 

while x0 < 100.0:
	vetor.append(x0)
	x0 = x0 + passo 
```

Ao executar esse programa vamos ter armazenado na variável `vetor` um vetor com as componentes iniciando em `0.0` aumentando em passos de `0.25`.



## Plotando gráficos 


Podemos utilzar esse conhecimento de criar vetores para criar pontos do gráfico de uma função. Por exemplo para a função $f(x) = x^2$ podemos criar um outro vetor vazio e colocar em suas componentes o valor de $x_0^2$ para cada componente correspondente ao seu valor no vetor $x$. 




