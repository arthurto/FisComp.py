import numpy as np
import matplotlib.pyplot as plt

# Definindo os parâmetros iniciais
r_values = np.linspace(2.5, 4.0, 10000)
iterations = 1000
last = 100

x = 1e-5 * np.ones(10000)

# Criando o gráfico
plt.figure(figsize=(10, 6))

# Executando as iterações do mapa logístico
for i in range(iterations):
    x = r_values * x * (1 - x)
    if i >= (iterations - last):
        plt.plot(r_values, x, ',k', alpha=0.25)

plt.title("Mapa Logístico")
plt.xlabel("Taxa de Reprodução (r)")
plt.ylabel("População (x)")
plt.xlim(2.5, 4.0)
plt.ylim(0, 1)
plt.show()

