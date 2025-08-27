# Análise de EDPs com Séries de Fourier

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Libraries](https://img.shields.io/badge/Libraries-NumPy%20%7C%20Matplotlib-orange)
![License](https://img.shields.io/badge/License-MIT-green)

Este repositório contém análises e simulações baseadas em Séries de Fourier, com foco na solução de Equações Diferenciais Parciais (EDPs) e na aproximação de funções. O projeto demonstra visualmente a convergência das séries e o famoso Fenômeno de Gibbs.

## 🎯 Conceitos Abordados

- **Série de Fourier**: Aproximação de funções periódicas (ou definidas em um intervalo) por uma soma de senos e cossenos.
- **Equação do Calor**: Solução da EDP unidimensional da difusão de calor com condições de contorno de Dirichlet homogêneas.
- **Fenômeno de Gibbs**: Análise do comportamento de overshoot da Série de Fourier próximo a descontinuidades.
- **Análise de Convergência**: Estudo do erro da aproximação em função do número de termos (`N`) da série.

## 📂 Estrutura do Repositório

Para evitar a repetição de código, as funções centrais foram consolidadas em um módulo de utilitários (`fourier_utils.py`). Os outros scripts, renomeados para maior clareza, importam essas funções para realizar análises específicas.

- **`fourier_utils.py`**: Módulo central com as implementações das séries.
  - `fourier_series_square_wave()`: Aproxima uma onda quadrada.
  - `solve_heat_equation()`: Resolve a equação do calor para uma condição inicial `f(x)`.

- **`1_square_wave_approximation.py`** (antigo `plot.py`):
  - Visualiza a aproximação de uma onda quadrada para diferentes números de termos (`N=5, 10, 20`).

- **`2_square_wave_error.py`** (antigo `ns.py`):
  - Calcula e plota o Erro Médio Quadrático (MSE) da aproximação da onda quadrada.
  - Compara o erro total com o erro em regiões contínuas para destacar o impacto do Fenômeno de Gibbs.

- **`3_heat_equation_simulation.py`** (antigo `sim.py`):
  - Simula a evolução temporal da temperatura em uma barra com uma distribuição inicial gaussiana.

- **`4_heat_equation_error.py`** (antigo `erro_relativo.py`):
  - Analisa como o erro relativo da solução da equação do calor diminui à medida que o número de termos `N` aumenta.

## 🚀 Como Executar

### Pré-requisitos

Certifique-se de que você tem o Python 3 e as bibliotecas necessárias instaladas.

```bash
pip install numpy matplotlib