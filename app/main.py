import random


def flip_coin() -> dict:
    result = {}
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            if random.choice(["head", "tail"]) == "head":
                heads += 1
        result[heads] = result.get(heads, 0) + 1
    print(result)
    result = {
        key: value / 10000 * 100
        for key, value in result.items()
    }
    print(result)

    return result
