import random


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}

    trials = 10000
    flips_per_trial = 10

    for _ in range(trials):
        heads = sum(1 for _ in range(flips_per_trial) if random.random() < 0.5)
        results[heads] += 1

    final_results = {}
    for key, value in results.items():
        percent = value / trials * 100

        noise = random.uniform(-0.01, 0.01)
        percent += noise

        percent = max(0, min(100, percent))

        final_results[key] = round(percent, 2)

    return final_results
