import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    results = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads = sum(random.randint(0, 1) for _ in range(10))
        results[heads] += 1

    return {k: (v / 10000) * 100 for k, v in results.items()}


def draw_gaussian_distribution_graph() -> None:
    wynik = flip_coin()

    lista_x = list(wynik.keys())
    lista_y = list(wynik.values())

    plt.bar(lista_x, lista_y)
    plt.show()
