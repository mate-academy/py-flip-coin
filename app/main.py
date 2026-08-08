import random

if __name__ == "__main__":
    from matplotlib import pyplot


def flip_coin() -> dict:
    flip_dict = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0
    }

    for _ in range(10000):
        heads = 0
        for _ in range(10):
            flip = random.randint(1, 2)
            if flip == 1:
                heads += 1
        flip_dict[heads] += 1

    flip_percent_dict = {key: item / 100 for key, item in flip_dict.items()}
    return flip_percent_dict


def draw_gaussian_distribution_graph(graph: dict) -> None:
    ypoints = [y for y in graph.values()]

    pyplot.title("Gaussian distribution")
    pyplot.xlabel("Heads count")
    pyplot.ylabel("Drop persentage %")

    pyplot.xlim(0, 10)
    pyplot.ylim(0, 100)

    pyplot.plot(ypoints)
    pyplot.show()
