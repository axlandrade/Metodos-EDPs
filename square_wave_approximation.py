# 1_square_wave_approximation.py

import numpy as np
import matplotlib.pyplot as plt
from fourier_utils import fourier_series_square_wave

# --- Definições ---
L = np.pi
x = np.linspace(-L, L, 1000)

def f_original(x):
    """ A função de onda quadrada original. """
    return np.where(x < 0, 1, -1)

# --- Configuração do Plot ---
fig, axs = plt.subplots(3, 1, figsize=(10, 10), sharex=True)
Ns = [5, 10, 20] # Número de termos para visualizar

for i, N in enumerate(Ns):
    # Calcula a aproximação da série
    sN = fourier_series_square_wave(x, N, L)
    
    # Plota os resultados
    axs[i].plot(x, f_original(x), label='Função Original $f(x)$', color='black', linewidth=2)
    axs[i].plot(x, sN, label=f'Série de Fourier (N = {N})', color='blue', linestyle='--')
    axs[i].set_title(f'Aproximação com N = {N} termos')
    axs[i].legend()
    axs[i].grid(True)
    axs[i].set_ylabel('f(x)')

plt.xlabel('x')
plt.suptitle('Aproximação de Onda Quadrada por Série de Fourier', fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.96])
plt.show()