import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    res = {num: 0 for num in range(11)}
    for one in range(1, 10001):
        heads = 0
        for flip in range(1, 11):
            fl = random.choice(["head", "tail"])
            if fl == "head":
                heads += 1
        res[heads] += 1
    for heads, value in res.items():
        res[heads] = value / 10000 * 100
    return res


def draw_gaussian_distribution_graph(res: dict) -> None:
    x_arr = [
        num for num, val in res.items()
    ]
    y_arr = [
        val for num, val in res.items()
    ]
    plt.plot(x_arr, y_arr)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()


if __name__ == "__main__":
    res = flip_coin()
    draw_gaussian_distribution_graph(res)
