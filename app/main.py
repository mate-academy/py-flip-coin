import random


def flip_coin(num_flips: int = 10, num_trials: int = 10000) -> dict:
    """Simulate flipping a coin `num_flips` times for `num_trials` trials."""
    results_count = {i: 0 for i in range(num_flips + 1)}
    for _ in range(num_trials):
        heads_count = 0
        for _ in range(num_flips):
            if random.random() < 0.5:
                heads_count += 1
        results_count[heads_count] += 1

    results_percent = {
        heads: round(count / num_trials * 100, 2)
        for heads, count in results_count.items()
    }
    return results_percent


def draw_gaussian_distribution_graph(distribution: dict) -> None:
    """Draw a bar graph showing the coin flip distribution."""
    import matplotlib.pyplot as plt

    heads_numbers = list(distribution.keys())
    percentages = list(distribution.values())

    plt.bar(heads_numbers, percentages)
    plt.xlabel('Number of heads')
    plt.ylabel('Percentage (%)')
    plt.title('Distribution of heads in 10 coin flips')
    plt.xticks(heads_numbers)
    plt.show()


if __name__ == '__main__':
    distribution = flip_coin()
    print(distribution)
    draw_gaussian_distribution_graph(distribution)
    
