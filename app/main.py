import random


def flip_coin() -> int:
    simulation_num = 10000
    results = {i: 0 for i in range(11)}
    for _ in range(simulation_num):
        heads_coin = sum(random.choice(["heads", "tails"])
                         == "heads" for _ in range(10))
        results[heads_coin] += 1
    for key in results:
        results[key] = round(results[key] / simulation_num * 100, 2)

    return results


print(flip_coin())
