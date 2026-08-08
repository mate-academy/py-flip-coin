import random

# import matplotlib.pyplot as plt


def flip_coin() -> dict:
    num_trials = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(num_trials):
        num_heads = sum(random.choice([0, 1]) for _ in range(10))
        results[num_heads] += 1

    percentages = {key: (value / num_trials) * 100
                   for key, value in results.items()}
    return percentages


# def draw_gaussian_distribution_graph(percentages: dict) -> None:
#     plt.bar(percentages.keys(), percentages.values())
#     plt.xlabel("Number of Heads")
#     plt.ylabel("Percentage")
#     plt.title("Gaussian Distribution of Coin Flips")
#     plt.show()
#
#
# if __name__ == "__main__":
#     percentages = flip_coin()
#     print(percentages)
#     draw_gaussian_distribution_graph(percentages)
