# Começando a programar 

Nesse arquivo estão listados alguns recursos para programar em python.

Muitas vezes a primeira barreira para a programação pode ser o fato de você nunca ter sido instruído sobre onde escrever o programa e como executá-lo. 
De forma simples, um programa em python pode ser escrito em um editor de texto e executado com uma linha de comando no terminal.

# Alguns conceitos importantes

### Editor de texto 

No editor de texto você pode escrever um programa em python e salvá-lo na extensão `.py`.
Um programa é um conjunto de instruções (algoritmo) escrito e estruturado de uma forma específica (sintaxe da linguagem) para ser executada ou compilada depois. 

### Terminal 

Podemos executar um programa no terminal utilizando o comando:
bash```python3 programa.py```

O terminal é um ambiente de input e output de dados. Os dados de input são os comandos e os outputs podem ser a execução dos programas ou a informação requisitada.
De forma simples, é uma forma de executar processos no computador através de comandos de texto.

## WSL - Usando Linux no Windows 

Caso o seu sistema operacional seja Windows 10 ou 11, como é no meu caso, é possível utilizar o WSL (Windows Subsistem for Linux). 
As instuções do [site oficial da Microsoft](https://learn.microsoft.com/pt-br/windows/wsl/install) podem ser úteis.

## Virtual Machine 

Outra possibilidade é a utilização de uma máquina virtual que emula outro sistema operacional para utilização dos programas em Linux. 
Programas como [VirtualBox](https://www.virtualbox.org/) podem ser instalados para isso.

### REPL 

É possível programar em python diretamente do terminal, utilizando o REPL. 

O REPL é uma sigla para "Read,Evaluate,Print,Loop", ou seja, ele lê, executa, imprime e espera o seu próximo comando para fazer tudo isso novamente. 
__A palavra "loop" ou "laço" aparece em um programa quando queremos dizer que um certo "pedaço" do programa vai ser repetido mais de uma vez.__

No REPL você escreve um programa linha por linha e ele vai sendo executado em tempo real. Esse tipo de execução de programas é melhor para testes rápidos de funcionalidades do que para programas relamente complexos, o melhor mesmo é utilizar algum editor de texto ou um IDE. 

### IDE 

Um IDE, ou Integrated Development Environment (ambiente integrado de desenvolvimento).
É um programa que combina no mesmo ambiente um editor de texto e ferramentas para execução do programa a ser desenvolvido, como um terminal integrado, na maioria dos casos.
Exemplos de IDEs: 
 
- VSCode 
- IDLE 
- Atom 
- PyCharm

Para poder executar python localmente em seu computador, é necessário instalar. 

## Python.org 

No [site oficial da linguagem python](https://www.python.org/) é possível baixar o interpretador de python para o seu computador pessoal.

Em um computador com sistema linux podemos instalar python pelo terminal com o comando 
bash```sudo apt-get install python3```

Também é possível executar blocos de programas em python na nuvem do Google, no site Google Collab. 

## Google Collab

No [Google Collab](https://colab.research.google.com/) temos acesso a um notebook que interpreta python online.
Muitas bibliotecas estão disponíveis e a colaboração entre diferentes colaboradores é facilitada. 

