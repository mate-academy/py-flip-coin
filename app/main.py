import random
from typing import Dict


def flip_coin(
    num_simulations: int = 10_000,
    num_flips: int = 10
) -> Dict[int, float]:

    results = {i: 0 for i in range(num_flips + 1)}

    for _ in range(num_simulations):
        heads = sum(random.choice([0, 1]) for _ in range(num_flips))
        results[heads] += 1

    return {
        heads: round((count / num_simulations) * 100, 2)
        for heads, count in results.items()
    }


def draw_gaussian_distribution_graph(distribution: Dict[int, float]) -> None:
    import matplotlib.pyplot as plt

    x_values = list(distribution.keys())
    y_values = list(distribution.values())

    plt.figure()
    plt.plot(x_values, y_values, marker="o")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xticks(x_values)
    plt.grid(True)
    plt.show()


def main() -> None:
    """
    Função principal do programa.
    """
    distribution = flip_coin()
    print(distribution)
    draw_gaussian_distribution_graph(distribution)


if __name__ == "__main__":
    main()
