import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    flip_dict = {heads: 0 for heads in range(11)}
    total_simulations = 10_000
    num_flips = 10

    for _ in range(total_simulations):
        count_heads = 0
        for _ in range(num_flips):
            if random.randint(0, 1) == 1:
                count_heads += 1
        flip_dict[count_heads] = flip_dict.get(count_heads, 0) + 1

    return {
        heads: round((count / total_simulations) * 100, 2)
        for heads, count in flip_dict.items()
    }

def draw_gaussian_distribution_graph() -> None:
    coins = flip_coin()
    heads = list(coins.keys())
    percentages = list(coins.values())

    plt.plot(heads, percentages, marker="o")
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage %")
    plt.title("Coin flip distribution")
    plt.show()

draw_gaussian_distribution_graph()