import random


def flip_coin() -> dict:
    result_dict = {i: 0 for i in range(0, 11)}
    for i in range(0, 10000):
        count = [random.randint(0, 1) for _ in range(0, 10)].count(1)
        result_dict[count] += 1
    print(result_dict)
    for key, value in result_dict.items():
        result_dict[key] = value / 100
    return result_dict


def draw_gaussian_distribution_graph(result: dict) -> None:
    import matplotlib
    iks = [key for key in result.keys()]
    igrik = [100 * value for value in result.values()]

    matplotlib.pyplot.plot(iks, igrik)

    matplotlib.pyplot.xlabel("Heads count")
    matplotlib.pyplot.ylabel("Drop percentage %")

    matplotlib.pyplot.show()
