from random import randint


def flip_coin() -> dict:
    distribution = {k: 0 for k in range(11)}
    for _ in range(10000):
        heads_count = 0
        for _ in range(10):
            if randint(0, 1) == 0:
                heads_count += 1
        distribution[heads_count] += 1
    for key in distribution:
        distribution[key] = (distribution[key] / 10000) * 100
    return distribution
