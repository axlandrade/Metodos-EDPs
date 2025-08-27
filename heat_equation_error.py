# 4_heat_equation_error.py

import numpy as np
import matplotlib.pyplot as plt
from fourier_utils import solve_heat_equation

# --- Parâmetros da Análise ---
L = 5.0
alpha = 1e-3
x = np.linspace(0, L, 500)
t_fixed = 0.1 # Instante de tempo fixo para a análise de erro

# Condição inicial
f0 = np.exp(-8 * (x - L/2)**2)

# --- Análise de Erro ---
# Solução de referência com um número muito grande de termos
N_ref = 200
T_reference = solve_heat_equation(x, t_fixed, N_ref, L, alpha, f0)

N_values = [5, 10, 20, 40, 80, 100]
relative_errors = []

for N in N_values:
    T_approx = solve_heat_equation(x, t_fixed, N, L, alpha, f0)
    # Calcula o erro relativo usando a norma L2
    error = np.linalg.norm(T_reference - T_approx) / np.linalg.norm(T_reference)
    relative_errors.append(error)

# --- Plot do Erro ---
plt.figure(figsize=(10, 6))
plt.plot(N_values, relative_errors, marker='o', linestyle='--')
plt.title(f'Erro Relativo da Solução da Equação do Calor em t = {t_fixed}s')
plt.xlabel('Número de Termos (N)')
plt.ylabel('Erro Relativo (Norma L2)')
plt.grid(True)
plt.yscale('log')
plt.show()