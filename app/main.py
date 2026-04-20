from random import randint


def flip_coin() -> dict:
    result = {0: 0,
              1: 0,
              2: 0,
              3: 0,
              4: 0,
              5: 0,
              6: 0,
              7: 0,
              8: 0,
              9: 0,
              10: 0}

    def ten_tries() -> int:
        heads = 0
        for throw in range(10):
            throw = randint(0, 1)
            if throw:
                heads += 1
        return heads

    for _ in range(10000):
        throws = ten_tries()
        result[throws] += 1

    for key, value in result.items():
        result[key] = round((value / 100), 2)
    return result
