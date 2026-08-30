import random


def flip_coin() -> dict:
    trials = 10000
    flips_per_trial = 10

    results = {i: 0 for i in range(flips_per_trial + 1)}

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(flips_per_trial))
        results[heads] += 1

    percentages = {
        k: round((v / trials) * 100, 2)
        for k, v in results.items()
    }

    return percentages


if __name__ == "__main__":
    print(flip_coin())
