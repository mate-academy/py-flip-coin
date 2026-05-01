import random


def flip_coin() -> dict:
    results = {}
    coin = ("head", "tail")
    no_of_cases = 10000
    no_of_drop = 10
    count_of_head_drops = []

    for _ in range(no_of_cases):
        head_drop_count = 0
        for _ in range(no_of_drop):
            if coin[random.randint(0, 1)] == "head":
                head_drop_count += 1
        count_of_head_drops.append(head_drop_count)

    for count in sorted(set(count_of_head_drops)):
        results[count] = round(
            count_of_head_drops.count(count) / no_of_cases * 100,
            2
        )

    return results
