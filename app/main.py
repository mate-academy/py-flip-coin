import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {key: 0 for key in range(11)}
    for _ in range(10000):
        count_head = 0
        for i in range(10):
            flip = random.choice(["head", "tail"])
            if flip == "head":
                count_head += 1
        result[count_head] += 1

    for key, value in result.items():
        result[key] = round((value / 10000) * 100, 2)
    return result


data = flip_coin()


def draw_gaussian_distribution_graph(data: dict) -> None:
    x_ = list(data.keys())
    y_ = list(data.values())
    plt.figure(figsize=(8, 5))
    plt.plot(x_, y_, marker="o", linestyle="-", color="blue")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)
    plt.ylim(0, 100)
    plt.show()
