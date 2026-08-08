import random
import matplotlib.pyplot


def flip_coin() -> dict[float, float]:
    trials = 10000
    flips_per_trial = 10
    result_counts = {i: 0 for i in range(flips_per_trial + 1)}

    for _ in range(trials):
        heads = sum(random.randint(0, 1) for _ in range(flips_per_trial))
        result_counts[heads] += 1

    for heads in result_counts:
        result_counts[heads] = round((result_counts[heads] / trials) * 100, 2)

    return result_counts


def draw_gaussian_distribution_graph(distribution: dict[float, float]) -> None:
    keys = sorted(distribution.keys())
    values = [distribution[k] for k in keys]

    matplotlib.pyplot.figure(figsize=(8, 5))
    matplotlib.pyplot.bar(keys, values, color="skyblue")
    matplotlib.pyplot.xlabel("Number of heads in 10 coin flips")
    matplotlib.pyplot.ylabel("Percentage of trials (%)")
    matplotlib.pyplot.title("Gaussian Distribution of Coin Flips")
    matplotlib.pyplot.xticks(keys)
    matplotlib.pyplot.show()


if __name__ == "__main__":
    distribution = flip_coin()
    print(distribution)
    draw_gaussian_distribution_graph(distribution)
