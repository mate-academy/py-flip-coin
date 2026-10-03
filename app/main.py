import random


def flip_coin(cases: int = 10000) -> dict:
    result = {heads: 0 for heads in range(11)}

    for _ in range(cases):
        heads_count = 0

        for _ in range(10):
            if random.choice(["heads", "tails"]) == "heads":
                heads_count += 1

        result[heads_count] += 1

    for heads_count in result:
        result[heads_count] = (
            result[heads_count] / cases * 100
        )

    return result
`
