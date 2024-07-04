import matplotlib.pyplot as plt
import numpy as np 

def func(x):
    return np.sin(x)

def num_deriv(f,x,h=1e-4):
    return (f(x+h)-f(x+h))/(2*h)

def num_deriv_order(f,x,n):
    if n == 0:
        return f(x)
    else: 
        return num_deriv()

def taylor_f(x,order):
    value = 0.0
    for i in range(order):
        n = i + 1 
        value += num_deriv(x)*(x**n)/np.math.factorial(n)

x = np.linspace(-2*np.pi,2*np.pi,100)


# Plota a função original
plt.plot(x,func(x),label = "função original")

# Define os valores do dimensionamento do plot 
plt.ylim(-5,5)
plt.xlim(-2*np.pi,2*np.pi)
plt.grid(alpha=0.3)
# mostra o plot
plt.show()