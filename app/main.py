import random
from collections import Counter
import matplotlib.pyplot as plt

# 1. Função de Simulação
def flip_coin(num_simulations=10000, n_flips=10):
    counts = Counter()
    for _ in range(num_simulations):
        heads = sum(random.choice([0, 1]) for _ in range(n_flips))
        counts[heads] += 1
        
    percentages = {
        k: round((counts[k] / num_simulations) * 100, 2) 
        for k in range(n_flips + 1)
    }
    return dict(sorted(percentages.items()))

# 2. Função de Gráfico
def draw_gaussian_distribution_graph(data_dict):
    heads = list(data_dict.keys())
    percentages = list(data_dict.values())
    
    plt.figure(figsize=(9, 5))
    plt.bar(heads, percentages, color='#4A90E2', edgecolor='#2C3E50', alpha=0.85, width=0.6)
    
    plt.xlabel('Número de Caras', fontsize=12, fontweight='bold')
    plt.ylabel('Porcentagem (%)', fontsize=12, fontweight='bold')
    plt.title('Distribuição de Probabilidade - Lançamento de Moedas (10 vezes)', fontsize=14, fontweight='bold')
    
    plt.xticks(heads)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    
    for x, y in zip(heads, percentages):
        plt.text(x, y + 0.5, f'{y}%', ha='center', va='bottom', fontsize=9)
        
    plt.ylim(0, max(percentages) + 6)
    plt.tight_layout()
    plt.show()

# Executando o fluxo:
resultado = flip_coin(10000)
print("Dicionário gerado:", resultado)
draw_gaussian_distribution_graph(resultado)
