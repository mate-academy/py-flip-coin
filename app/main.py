import random

NUMBER_OF_FLIPS = 10
NUMBER_OF_EXPERIMENTS = 10_000


def flip_coin() -> dict[int, float]:
    heads_counts = {}

    for number_of_heads in range(NUMBER_OF_FLIPS + 1):
        heads_counts[number_of_heads] = 0

    for _ in range(NUMBER_OF_EXPERIMENTS):
        number_of_heads = 0

        for _ in range(NUMBER_OF_FLIPS):
            coin_side = random.choice(("heads", "tails"))

            if coin_side == "heads":
                number_of_heads += 1

        heads_counts[number_of_heads] += 1

    percentages = {}

    for number_of_heads, count in heads_counts.items():
        percentage = count / NUMBER_OF_EXPERIMENTS * 100
        percentages[number_of_heads] = round(percentage, 2)

    return percentages


def draw_gaussian_distribution_graph() -> None:
    import matplotlib.pyplot as plt

    distribution = flip_coin()

    plt.bar(distribution.keys(), distribution.values())
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage of experiments")
    plt.title("Distribution of heads in 10 coin flips")
    plt.xticks(range(NUMBER_OF_FLIPS + 1))
    plt.show()
