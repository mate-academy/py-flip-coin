import random


def flip_coin() -> dict:
    def dice_rolls(cnt: int) -> list[int]:
        return [random.randint(0, 1) for _ in range(cnt)].count(1)

    cases = 10000
    sequence = 10

    result = {i: 0 for i in range(11)}
    for _ in range(cases):
        result[dice_rolls(sequence)] += 1
    result = {idx: el * 100 / cases for idx, el in result.items()}
    return result
