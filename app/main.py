import random


def flip_coin() -> dict:
    coin = ["heads", "tails"]
    times_of_heads = {i: 0 for i in range(11)}

    for i in range(1, 10001):
        counter = 0
        for _ in range(1, 11):
            if random.choice(coin) == "heads":
                counter += 1

        times_of_heads[counter] += 1

    for i in times_of_heads:
        times_of_heads[i] = round(times_of_heads[i] / 10000 * 100, 2)

    return times_of_heads
