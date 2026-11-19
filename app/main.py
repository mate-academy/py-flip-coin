import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results: dict[int, float] = {i: 0 for i in range(11)}
    experiments = 10000

    for _ in range(experiments):
        heads = 0

        for _ in range(10):
            if random.choice(["heads", "tails"]) == "heads":
                heads += 1

        results[heads] += 1

    for key in results:
        results[key] = round(results[key] / experiments * 100, 2)

    return results


def draw_gaussian_distribution_graph() -> None:
    results = flip_coin()

    plt.bar(results.keys(), results.values())
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage (%)")
    plt.title("Coin Flip Distribution")
    plt.show()


if __name__ == "__main__":
    print(flip_coin())
    draw_gaussian_distribution_graph()
