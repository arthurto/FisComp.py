from scipy.integrate import solve_ivp
import numpy as np 
import matplotlib.pyplot as plt
# Constantes
g = 9.81  # aceleração devido à gravidade (m/s^2)
b = 0.1   # coeficiente de resistência do ar (proporcional ao quadrado da velocidade)

# Condições iniciais
v0 = 30  # velocidade inicial (m/s)
angle = 45  # ângulo de lançamento em graus
vx0 = v0 * np.cos(np.radians(angle))  # velocidade inicial x
vy0 = v0 * np.sin(np.radians(angle))  # velocidade inicial y
y0 = 0  # posição inicial y (altura)
x0 = 0  # posição inicial x

# Equações do movimento
def motion(t, Y):
    x, vx, y, vy = Y
    dvx_dt = -b * vx * np.sqrt(vx**2 + vy**2)
    dvy_dt = -g - b * vy * np.sqrt(vx**2 + vy**2)
    dx_dt = vx
    dy_dt = vy
    return [dx_dt, dvx_dt, dy_dt, dvy_dt]

# Intervalo de tempo para a simulação
t_span = (0, 3)  # tempo total de 5 segundos
t_eval = np.linspace(*t_span, 1000)  # 1000 pontos de tempo para avaliação

# Resolvendo as equações de movimento
sol = solve_ivp(motion, t_span, [x0, vx0, y0, vy0], t_eval=t_eval, method='RK45')

# Plotando o gráfico da trajetória
plt.figure(figsize=(10, 6))
plt.plot(sol.y[0], sol.y[2], label='Trajetória com Atrito')
plt.title("Lançamento Oblíquo com Atrito")
plt.xlabel("Distância Horizontal (m)")
plt.ylabel("Altura (m)")
plt.legend()
plt.grid(True)
plt.show()

