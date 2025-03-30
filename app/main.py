from random import choice


def flip_coin() -> dict:
    out = {}
    for _ in range(10000):
        heads = sum(choice([0, 1]) for _ in range(10))
        out.update({heads: out.get(heads, 0) + 1})
    for heads in out:
        out[heads] = (out[heads] / 100)
    return out
