import numpy as np
import matplotlib.pyplot as plt

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

fig, axs = plt.subplots(3, 1, figsize=(10, 10), sharex=True)
Ns = [5, 10, 20]
for i, N in enumerate(Ns):
    axs[i].plot(x, f_original(x), label='f(x)', color='black', linewidth=2)
    axs[i].plot(x, fourier_series(x, N, L), label=f'N = {N}', color='blue')
    axs[i].set_title(f'Soma Parcial com N = {N}')
    axs[i].legend()
    axs[i].grid(True)

plt.xlabel('x')
plt.tight_layout()
plt.show()