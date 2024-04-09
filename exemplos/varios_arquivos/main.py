# Adicionando a função 
# definida em 'func.py'

# Existem duas formas de importar 
# funções de um arquivo 
# a primeira importa todas as funções
# mas é necessário expecificar o arquivo 
# "import func" -> "func.f"
# a outra forma é importando o arquivo direto
# 
# "from func import f" -> "f"
# ou posso apelidar o "func" como "fu". 
# 
# import func as fu 
# "fu.f(x)" 

from func import f

def main():
    # Essa função vai pegar os valores de x da f(x) 
    # e escrever o arquivo 
    # Progresso: 
    # [x] - func.py (desenvolvido) 
    # [ ] - gera_arquivo.py (não desenvolvido) 
    print("----- programa em desenvolvimento ------")
    
if __name__ == '__main__':
    main()
