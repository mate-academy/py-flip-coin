import random
from collections import defaultdict
import matplotlib.pyplot as plt


def flip_coin(number_of_flips: int = 10,
              number_of_trials: int = 10000) -> dict[int, float]:
    results_counter = defaultdict(int)

    for _ in range(number_of_trials):
        heads_count = sum(random.choice([0, 1])
                          for _ in range(number_of_flips))
        results_counter[heads_count] += 1

    percentages = {
        number_of_heads: round(trial_count / number_of_trials * 100, 2)
        for number_of_heads, trial_count in results_counter.items()
    }

    # Убедимся, что все значения от 0 до number_of_flips есть
    for heads_number in range(number_of_flips + 1):
        if heads_number not in percentages:
            percentages[heads_number] = 0.0

    return dict(sorted(percentages.items()))


def draw_gaussian_distribution_graph(distribution: dict[int, float]) -> None:
    heads_numbers = list(distribution.keys())
    percentages_values = list(distribution.values())

    plt.bar(heads_numbers, percentages_values, color="skyblue")
    plt.xlabel("Number of heads in 10 flips")
    plt.ylabel("Percentage of trials (%)")
    plt.title("Distribution of Heads in 10 Coin Flips")
    plt.xticks(heads_numbers)
    plt.show()


# Пример использования
distribution = flip_coin()
print(distribution)
draw_gaussian_distribution_graph(distribution)
