import random


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
        count = 0
        for _ in range(10):
            coin_side = random.randint(0, 1)
            if coin_side == 1:
                count += 1
        result[count] += 1
    for key, value in result.items():
        result[key] = (value / 10000) * 100
    return result


def draw_gaussian_distribution_graph() -> None:
    import matplotlib.pyplot as plt
    points = flip_coin()
    y_points = [value for value in points.values()]

    plt.plot(y_points)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.show()
