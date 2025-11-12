import random


def run_flip_coin() -> int:
    count_of_heads = 0
    for _ in range(10):
        heads = random.choice(["Heads", "Tails"])
        if heads == "Heads":
            count_of_heads += 1
    return count_of_heads


def flip_coin(n_runs: int = 10000) -> dict:
    dictionary = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0,
                  5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0
                  }
    for _ in range(n_runs):
        dictionary[run_flip_coin()] += 1
    for key, value in dictionary.items():
        dictionary[key] = round(value / n_runs * 100, 2)
    return dictionary
