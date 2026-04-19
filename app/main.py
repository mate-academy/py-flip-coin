import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    flip_dict = {i: 0 for i in range(11)}

    for _ in range(10000):
        n_heads = 0

        for _ in range(10):
            result = random.randint(0, 1)
            if result:
                n_heads += 1
        flip_dict[n_heads] = flip_dict.get(n_heads, 0) + 1
    persent_dict = {key: value / 100 for key, value in flip_dict.items()}
    return persent_dict


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    heads_count = list(data.keys())
    percentages = list(data.values())

    plt.figure(figsize=(10, 6))
    plt.plot(
        heads_count,
        percentages,
        color="red",
        linewidth=2,
        marker="o",
        label="Траєкторія результатів"
    )
    plt.bar(
        heads_count,
        percentages,
        color="skyblue",
        alpha=0.3,
        label="Експериментальні дані"
    )
    plt.title("Gaussian distribution graph")
    plt.xlabel("Кількість випадань 'Орла'")
    plt.ylabel("Відсоток (%)")
    plt.xticks(range(11))
    plt.legend()
    plt.grid(axis="y", alpha=0.3)

    plt.show()


if __name__ == "__main__":
    draw_gaussian_distribution_graph()
