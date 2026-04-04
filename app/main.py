from random import randint


def flip_a_coin() -> int:
    result = []
    for i in range(10):
        result += [randint(0, 1)]
    return sum(result)


def flip_coin() -> dict:
    counts = {}
    for i in range(10000):
        num = flip_a_coin()
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    for num in counts:
        counts[num] = round(counts[num] / 10000 * 100, 2)
    return dict(sorted(counts.items()))


def draw_gaussian_distribution_graph() -> None:
    import matplotlib.pyplot as plt
    points = flip_coin()
    xpoints = list(points.keys())
    ypoints = list(points.values())
    plt.plot(xpoints, ypoints)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
