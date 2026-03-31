import random


def flip_once() -> int:
    heads = 0
    for i in range(10):
        result = random.choice([0, 1])
        if result == 1:
            heads += 1
    return heads


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads = flip_once()
        results[heads] += 1

    for key in results:
        results[key] = round(results[key] / 10000 * 100, 2)
    return results


def count_results(results: list) -> dict:
    counts = {i: 0 for i in range(11)}
    for result in results:
        counts[result] += 1
    return counts


def to_percentages(counts: dict, total: int) -> dict:
    percentages = {}
    for i in counts:
        percentages[i] = round((counts[i] / total) * 100, 2)
    return percentages


if __name__ == "__main__":
    results = flip_coin()
    counts = count_results(results)
    percentages = to_percentages(counts, len(results))
    print(percentages)
