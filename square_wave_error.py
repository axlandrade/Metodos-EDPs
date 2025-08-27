# 2_square_wave_error.py

import numpy as np
import matplotlib.pyplot as plt
from fourier_utils import fourier_series_square_wave

# --- Definições ---
L = np.pi
x = np.linspace(-L, L, 1000)

def f_original(x):
    """ A função de onda quadrada original. """
    return np.where(x < 0, 1, -1)

def mse(f, g):
    """ Calcula o Erro Médio Quadrático entre duas funções. """
    return np.mean((f - g)**2)

def mse_continuous_part(f, g, x, delta=0.1):
    """ Calcula o MSE excluindo a vizinhança da descontinuidade. """
    # Máscara para selecionar pontos longe da descontinuidade em x=0
    mask = np.abs(x) > delta
    return np.mean((f[mask] - g[mask])**2)

# --- Análise de Erro ---
N_values = [5, 10, 20, 40, 80, 100]
f_vals = f_original(x)
errors_total = []
errors_continuous = []

for N in N_values:
    sN = fourier_series_square_wave(x, N, L)
    errors_total.append(mse(f_vals, sN))
    errors_continuous.append(mse_continuous_part(f_vals, sN, x, delta=0.1))

# --- Plot do Erro ---
plt.figure(figsize=(10, 6))
plt.plot(N_values, errors_total, marker='o', linestyle='--', label='Erro Total (inclui Fenômeno de Gibbs)')
plt.plot(N_values, errors_continuous, marker='s', linestyle='-', label='Erro em Partes Contínuas (exclui Gibbs)')
plt.title('Convergência do Erro Médio Quadrático vs. Número de Termos (N)')
plt.xlabel('Número de Termos (N)')
plt.ylabel('Erro Médio Quadrático (MSE)')
plt.legend()
plt.grid(True)
plt.yscale('log')
plt.show()