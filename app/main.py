import random


def flip_coin(num_simulations: int = 10000, num_flips: int = 10) -> dict:
    results = {key: 0 for key in range(num_flips + 1)}
    for _ in range(num_simulations):
        flips = [random.choice(["H", "T"]) for _ in range(num_flips)]
        num_heads = flips.count("H")
        results[num_heads] += 1
    for key in results:
        results[key] = (results[key] / num_simulations) * 100
    return results


data = flip_coin()
print(data)
