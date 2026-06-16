import random
from typing import Dict
# import matplotlib.pyplot as plt


def flip_coin(iterations: int = 10_000, flips: int = 10) -> Dict[int, float]:
    frequency = {
        i: 0
        for i in range(flips + 1)
    }

    # 10k iteration of flipping sessions
    for _ in range(iterations):

        frequency_of_heads = 0

        # 10 flips of coin
        for _ in range(flips):
            # imitation of flip
            flip_result = random.choice(["head", "not head"])
            frequency_of_heads += 1 if flip_result == "head" else 0

        # collecting result of coin flipping session
        frequency[frequency_of_heads] += 1

    for key in frequency:
        frequency[key] = round((frequency[key] / iterations) * 100, 2)

    return frequency


# def draw_gaussian_distribution_graph(frequency: Dict[int, float]) -> None:
#     plt.plot(list(frequency.keys()),
#              list(frequency.values()), marker="o",
#              linestyle="-", color="#915bd4")
#     plt.xlabel("Heads count")
#     plt.ylabel("Percentage %")
#     plt.title("Gaussian distribution")
#     plt.grid(linewidth=.75, alpha=.4)
#     plt.show()
