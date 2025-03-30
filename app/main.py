import random
import matplotlib.pyplot as plt


def flip_coin():
    tosses = 10
    quantity_experiment = 10000
    experiments_results = {
        count: 0 for count in range(tosses + 1)
    }
    for _ in range(quantity_experiment):
        toss_result = {"head": 0, "tail": 0}
        for toss in range(tosses):
            toss_result[random.choice(("head", "tail"))] += 1
        experiments_results[toss_result["head"]] += 1

    for key in experiments_results:
        experiments_results[key] = round(
            (experiments_results[key] / quantity_experiment) * 100, 2
        )

    return experiments_results


def draw_gaussian_distribution_graph():
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(*zip(*flip_coin().items()))
    plt.ylim([0, 100])
    plt.ylabel("Drop percentage %", fontsize=14)
    plt.xlabel("Heads count", fontsize=14)
    plt.show()


if __name__ == '__main__':
    print(flip_coin())
    draw_gaussian_distribution_graph()
