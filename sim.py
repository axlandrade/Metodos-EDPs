import numpy as np
import matplotlib.pyplot as plt

L = 5
alpha = 1e-3
x = np.linspace(0, L, 500)
times = [0.001, 0.01, 0.1, 0.5, 1.0]

f0 = np.exp(-8 * (x - 2.5)**2)

def T_series(x, t, N=50):
    result = np.zeros_like(x)
    for n in range(1, 2*N, 2):
        An = (2/L) * np.trapz(f0 * np.sin(n * np.pi * x / L), x)
        result += An * np.sin(n * np.pi * x / L) * np.exp(-alpha * (n * np.pi / L)**2 * t)
    return result

plt.figure(figsize=(10, 6))
for t in times:
    plt.plot(x, T_series(x, t), label=f't = {t}')
plt.title('Solução T(x,t) em diferentes tempos')
plt.xlabel('x')
plt.ylabel('T(x,t)')
plt.legend()
plt.grid()
plt.show()