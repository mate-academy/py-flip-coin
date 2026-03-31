import random


def flip_coin():
    rounds = []

    for _ in range(10_000):
        round_result = 0

        for _ in range(10):
            if random.randint(1, 2) == 1:
                round_result += 1

        rounds.append(round_result)

    percentage_of_cases = {
        x: (rounds.count(x) / (len(rounds) / 100)) for x in range(11)
    }

    return percentage_of_cases
