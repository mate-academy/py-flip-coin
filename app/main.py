import random


def flip_coin(num_trials: int = 10000) -> int:
    results = {i: 0 for i in range(11)}

    for _ in range(num_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    percentages = {key: (value / num_trials) * 100
                   for key, value in results.items()}
    return percentages


if __name__ == "__main__":
    pass
