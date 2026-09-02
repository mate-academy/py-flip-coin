
import random
import matplotlib.pyplot as plt


def flip_coin(num_trials: int = 10000) -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(num_trials):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        results[heads] += 1

    return {k: round(v / num_trials * 100, 2) for k, v in results.items()}


def draw_gaussian_distribution_graph(data: dict = None) -> None:
    if data is None:
        data = flip_coin()

    plt.bar(data.keys(), data.values())
    plt.xlabel("Número de caras em 10 lançamentos")
    plt.ylabel("Porcentagem (%)")
    plt.title("Distribuição de caras em 10 lançamentos de moeda")
    plt.show()


if __name__ == "__main__":
    print(flip_coin())
    draw_gaussian_distribution_graph()
