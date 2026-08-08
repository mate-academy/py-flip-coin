import random
import matplotlib.pyplot as plt


def flip_coin(number_of_cases: int = 10000,
              flips_per_case: int = 10) -> dict[int, float]:
    """
    Simulates coin flipping.
    Returns dictionary where:
    key = number of heads (0..10)
    value = percentage of cases
    """
    if number_of_cases < 1:
        raise ValueError("number_of_cases must be >= 1")
    if flips_per_case < 1:
        raise ValueError("flips_per_case must be >= 1")

    results: dict[int, int] = {heads_count: 0 for heads_count
                               in range(flips_per_case + 1)}

    for case_index in range(number_of_cases):
        heads_in_case = 0

        for flip_index in range(flips_per_case):
            coin_result = random.randint(0, 1)
            heads_in_case += coin_result

        results[heads_in_case] += 1

    percentages: dict[int, float] = {}

    for heads_count, cases_amount in results.items():
        percentage = (cases_amount / number_of_cases) * 100
        percentages[heads_count] = round(percentage, 2)

    return percentages


def draw_gaussian_distribution_graph(distribution: dict[int, float]) -> None:
    """
    Draws distribution graph using matplotlib.
    """
    head_numbers = sorted(distribution.keys())
    percentages = [distribution[number_of_heads] for
                   number_of_heads in head_numbers]

    plt.figure()
    plt.bar(head_numbers, percentages)
    plt.title("Distribution of heads in 10 coin flips")
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage (%)")
    plt.xticks(head_numbers)
    plt.grid(axis="y", linestyle="--", linewidth=0.5)
    plt.show()


if __name__ == "__main__":
    distribution_result = flip_coin()
    print(distribution_result)
    draw_gaussian_distribution_graph(distribution_result)
