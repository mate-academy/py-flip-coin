from random import choice


def flip_coin() -> dict:
    cases = 10_000
    coin_flips = {key: 0 for key in range(11)}

    for case in range(cases):
        count_heads = sum(
            1
            for head in range(10)
            if choice(["heads", "tails"]) == "heads"
        )
        coin_flips[count_heads] += 1

    coin_flips = {
        key: round((value / cases) * 100, 2)
        for key, value in coin_flips.items()
    }

    return coin_flips
