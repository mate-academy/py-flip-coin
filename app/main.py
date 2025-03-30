import random
import matplotlib.pyplot as plt


def flip_coin():
    flips = 10
    quantity_experiment = 10000
    experiment_result = {flip: 0 for flip in range(flips + 1)}
    for _ in range(quantity_experiment):
        flips_result = {"head": 0, "tail": 0}
        for flip in range(flips):
            flips_result[random.choice(("head", "tail"))] += 1
        experiment_result[flips_result["head"]] += 1

    for frequency, value in experiment_result.items():
        experiment_result[frequency] = round(
            (value / quantity_experiment) * 100, 2)

    return experiment_result


def draw_gaussian_distribution_graph():
    graph = flip_coin()

    fig, axes = plt.subplots()
    plt.ylim([0, 100])
    plt.xlim([0, 10])
    plt.xticks(list(range(11)))
    plt.yticks(list(range(0, 101, 10)))
    plt.plot(*zip(*graph.items()))

    plt.title("Gaussian distribution")
    axes.set_xlabel("Heads count")
    axes.set_ylabel("Drop percentage %")

    plt.show()


if __name__ == "__main__":
    print(flip_coin())
    draw_gaussian_distribution_graph()
