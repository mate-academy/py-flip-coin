import random
if __name__ == "__main__":
    import matplotlib.pyplot as plt


def flip_coin() -> dict:
    count_iteration = 10_000
    result = {key: 0 for key in range(10 + 1)}

    for _ in range(count_iteration):
        temp_result = 0
        for _ in range(10):
            temp_random = random.randint(1, 2)
            if temp_random != 1:
                temp_result += 1
        result[temp_result] += 1

    for key, value in result.items():
        result[key] = round(value * 100 / count_iteration, 2)

    return result


def draw_gaussian_distribution_graph(data: dict) -> None:
    x_data = []
    y_data = []
    for key, value in data.items():
        x_data.append(key)
        y_data.append(value)

    plt.figure(figsize=(10, 5))  # size of screen
    plt.plot(x_data, y_data, "", alpha=1, label="Gaussian distribution")
    plt.legend()
    plt.grid(True)
    plt.show()
    plt.savefig("test.png")


if __name__ == "__main__":
    result = flip_coin()
    print(result)
    print(draw_gaussian_distribution_graph(result))
