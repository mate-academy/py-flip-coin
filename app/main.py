import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    total_cases = 10000

    results = {heads: 0 for heads in range(11)}

    for case in range(total_cases):
        heads_count = 0

        for toss in range(10):
            coin = random.choice([0, 1])

            if coin == 1:
                heads_count += 1

        results[heads_count] += 1

    for heads_count in results:
        results[heads_count] = round(
            results[heads_count] / total_cases * 100, 2
        )

    return results


def draw_gaussian_distribution_graph() -> None:
    results = flip_coin()

    number_of_heads = list(results.keys())
    percentages = list(results.values())

    plt.bar(number_of_heads, percentages)

    plt.xlabel("Number of heads")
    plt.ylabel("Percentage (%)")
    plt.title("Coin Flip Distribution")

    plt.show()


# print(flip_coin())

# draw_gaussian_distribution_graph()
