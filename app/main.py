def flip_coin() -> dict:
    import random

    iterations_count = 10000
    results = {i: 0 for i in range(10)}

    for iteration in range(iterations_count):
        flip_sum = sum(
            random.choice([1, 0])  # head or not
            for _ in range(10)
        )
        if flip_sum not in results:
            results[flip_sum] = 0
        results[flip_sum] += 1

    for key in results:
        results[key] = results[key] / 10000 * 100

    return results


def draw_gaussian_distribution_graph(data: dict) -> None:
    import matplotlib.pyplot as plt

    points_data = list(data.values())

    y_points = points_data

    plt.plot(y_points)

    plt.axis([0, 10, 0, 100])

    plt.xticks(range(11))
    plt.yticks(range(0, 101, 10))

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
