# 3_heat_equation_simulation.py

import numpy as np
import matplotlib.pyplot as plt
from fourier_utils import solve_heat_equation

# --- Parâmetros da Simulação ---
L = 5.0
alpha = 1e-3
x = np.linspace(0, L, 500)
times = [0.001, 0.01, 0.1, 0.5, 1.0, 5.0]
N_terms = 50 # Número de termos na série para a simulação

# Condição inicial: um pulso Gaussiano centrado
f0 = np.exp(-8 * (x - L/2)**2)

# --- Simulação e Plot ---
plt.figure(figsize=(12, 7))
plt.plot(x, f0, label='Condição Inicial (t=0)', color='black', linestyle=':')

for t in times:
    T = solve_heat_equation(x, t, N_terms, L, alpha, f0)
    plt.plot(x, T, label=f't = {t} s')

plt.title('Solução da Equação do Calor Unidimensional')
plt.xlabel('Posição (x)')
plt.ylabel('Temperatura T(x,t)')
plt.legend()
plt.grid(True)
plt.show()