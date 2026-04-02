import random
import matplotlib.pyplot as plt


def flip_coin(number_of_experiments: int = 10000) -> dict:
    dict_heads = {n: 0 for n in range(11)}
    for _ in range(number_of_experiments):
        heads_in_one_trial = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                heads_in_one_trial += 1
        dict_heads[heads_in_one_trial] += 1
    for key, value in dict_heads.items():
        dict_heads[key] = round(value / number_of_experiments * 100, 2)

    return dict_heads


def draw_gaussian_distribution_graph(points: dict) -> None:
    x_lim = list(points.keys())
    y_lim = [int(v) for v in points.values()]

    plt.figure(figsize=(8, 5))
    plt.plot(
        x_lim,
        y_lim,
        color="red",
        marker="o",
        label="Data"
    )  # лінія з маркерами
    plt.xlabel("X (0–10)")
    plt.ylabel("Y (0–100)")
    plt.title("Графік зі словника")
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.grid(True)
    plt.legend()  # щоб показати підпис лінії
    plt.show()
