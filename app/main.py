"""Módulo para simulação de lançamento de moedas e representação gráfica."""

from collections import Counter
import random

import matplotlib.pyplot as plt


def flip_coin(num_simulations: int = 10000, n_flips: int = 10) -> dict:
    """Simula lançamentos de moedas e devolve as percentagens de caras."""
    counts = Counter()

    for simulation_index in range(num_simulations):
        heads_count = sum(
            random.choice([0, 1]) for flip_index in range(n_flips)
        )
        counts[heads_count] += 1

    percentages = {
        heads_val: round((counts[heads_val] / num_simulations) * 100, 2)
        for heads_val in range(n_flips + 1)
    }

    return dict(sorted(percentages.items()))


def draw_gaussian_distribution_graph(data_dict: dict) -> None:
    """Desenha um gráfico de barras com a distribuição dos lançamentos."""
    heads = list(data_dict.keys())
    percentages = list(data_dict.values())

    plt.figure(figsize=(9, 5))
    plt.bar(
        heads,
        percentages,
        color="#4A90E2",
        edgecolor="#2C3E50",
        alpha=0.85,
        width=0.6,
    )

    plt.xlabel("Número de Caras", fontsize=12, fontweight="bold")
    plt.ylabel("Porcentagem (%)", fontsize=12, fontweight="bold")
    plt.title(
        "Distribuição de Probabilidade - Lançamento de Moedas (10 vezes)",
        fontsize=14,
        fontweight="bold",
    )

    plt.xticks(heads)
    plt.grid(axis="y", linestyle="--", alpha=0.6)

    for head_val, percentage_val in zip(heads, percentages):
        plt.text(
            head_val,
            percentage_val + 0.5,
            f"{percentage_val}%",
            ha="center",
            va="bottom",
            fontsize=9,
        )

    plt.ylim(0, max(percentages) + 6)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    resultado = flip_coin(10000)
    draw_gaussian_distribution_graph(resultado)
