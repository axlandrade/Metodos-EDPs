import numpy as np
import matplotlib.pyplot as plt

L = 5
alpha = 1e-3
x = np.linspace(0, L, 500)
t = 0.1
f0 = np.exp(-8 * (x - 2.5)**2)

# Solução exata como referência com N grande
def T_series(x, t, N=200):
    result = np.zeros_like(x)
    for n in range(1, 2*N, 2):
        An = (2/L) * np.trapz(f0 * np.sin(n * np.pi * x / L), x)
        result += An * np.sin(n * np.pi * x / L) * np.exp(-alpha * (n * np.pi / L)**2 * t)
    return result

T_exact = T_series(x, t, N=200)

Ns = [5, 10, 20, 40, 80, 100]
errors = []
for N in Ns:
    T_approx = T_series(x, t, N=N)
    error = np.linalg.norm(T_exact - T_approx) / np.linalg.norm(T_exact)
    errors.append(error)

plt.figure()
plt.plot(Ns, errors, marker='o')
plt.title('Erro relativo vs número de termos N')
plt.xlabel('N')
plt.ylabel('Erro relativo')
plt.grid()
plt.show()