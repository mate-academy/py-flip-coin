import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        count = 0
        for flip in range(10):
            coin_head = random.choice(["head", "tail"])
            if coin_head == "head":
                count += 1
        result[count] += 1
    for heads, value in result.items():
        result[heads] = (value / 10000) * 100
    return result


def draw_gaussian_distribution_graph(points: dict) -> plt.Figure:
    plt.title("Gaussian Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    xpoints = list(points.keys())
    ypoints = list(points.values())
    plt.plot(xpoints, ypoints)
    plt.ylim(0, 100)
    plt.show()
