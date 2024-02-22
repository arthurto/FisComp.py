import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def main():
    # Tamanho da imagem (em pixels)
    largura, altura = 800, 600

    # Limites do plano complexo que queremos visualizar
    x_min, x_max = -2, 1
    y_min, y_max = -1.5, 1.5

    # Cria um array para armazenar os valores dos pixels
    imagem = np.zeros((altura, largura))

    # Define o número máximo de iterações
    max_iter = 100

    # Gera os valores para cada pixel
    for i in range(altura):
        for j in range(largura):
            c = complex(x_min + (x_max - x_min) * j / largura, y_min + (y_max - y_min) * i / altura)
            imagem[i, j] = mandelbrot(c, max_iter)

    # Mostra a imagem
    plt.imshow(imagem, cmap='hot', extent=(x_min, x_max, y_min, y_max))
    plt.colorbar()
    plt.title("Conjunto de Mandelbrot")
    plt.xlabel("Re(c)")
    plt.ylabel("Im(c)")
    plt.show()

if __name__=="__main__":
    main()
