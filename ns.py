import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

L = np.pi
x = np.linspace(-L, L, 1000)

def f_original(x):
    return np.where(x < 0, 1, -1)

def fourier_series(x, N, L):
    result = np.zeros_like(x)
    for n in range(1, 2*N, 2):
        bn = 4 / (n * np.pi)
        result += bn * np.sin(n * np.pi * x / L)
    return result

def mse(f, g):
    return np.mean((f - g)**2)

def mse_continuo(f, g, x, delta=0.1):
    # Exclui pontos próximos à descontinuidade em x=0
    mask = np.abs(x) > delta
    return np.mean((f[mask] - g[mask])**2)

errors = []
errors_continuo = []
N_values = [5, 10, 20, 40, 80, 100]
f_vals = f_original(x)

for N in N_values:
    sN = fourier_series(x, N, L)
    errors.append(mse(f_vals, sN))
    errors_continuo.append(mse_continuo(f_vals, sN, x, delta=0.1))

plt.figure()
plt.plot(N_values, errors, marker='o', label='Erro total (com Gibbs)')
plt.plot(N_values, errors_continuo, marker='s', label='Erro só onde é contínua')
plt.title('Erro médio quadrático vs N')
plt.xlabel('N')
plt.ylabel('Erro')
plt.legend()
plt.grid()
plt.show()