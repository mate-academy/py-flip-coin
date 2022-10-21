from random import choice

import matplotlib.pyplot as plt


def head_flipped() -> bool:
    result = 0
    coin = ["head", "tail"]
    for _ in range(10):
        if choice(coin) == "head":
            result += 1
    return result


def flip_coin() -> dict:
    result = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }
    for _ in range(10000):
        count = head_flipped()
        if count in result:
            result[count] += 1
    for key, value in result.items():
        result[key] = round(value / 10000 * 100, 2)
    return result


def draw_gaussian_distribution_graph() -> None:
    coordinates = flip_coin()
    point_x = [key for key in coordinates.keys()]
    point_y = [value for value in coordinates.values()]

    dpi = 80
    fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))

    plt.axis([0, 10, 0, 100])

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage, %")

    plt.plot(
        point_x,
        point_y,
        "o-b",
        alpha=0.7,
        label="first",
        lw=5,
        mec="r",
        mew=1,
        ms=10
    )
    plt.legend()
    plt.grid(True)
    fig.savefig("gaussian_distribution.png")
