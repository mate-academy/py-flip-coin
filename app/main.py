from random import choices


def flip_coin(series: int = 10000) -> dict:
    result = {}
    for num in range(series):
        attempt = choices([0, 1], k=10)
        head_count = attempt.count(1)
        result[head_count] = result.get(head_count, 0) + 1
    return {
        key:round(value / series * 100, 2)
        for key, value in sorted(result.items())
    }