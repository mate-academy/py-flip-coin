from random import choice


def flip_coin() -> dict[str, int]:
    result = {}
    for i in range(0, 10000):
        counter = 0
        for _ in range(10):
            flip = choice(["H", "T"])
            if flip == "H":
                counter += 1
        result[counter] = result.get(counter, 0) + 1
    for key in result:
        result[key] = (result[key] / 10000) * 100

    return result
