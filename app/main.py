import random
from typing import Dict


def flip_coin() -> Dict[int, int]:
    dict_heads = {i: 0 for i in range(10)}
    for qwe in range(10000):
        heads = 0
        for i in range(10):
            if random.randint(0, 1) == 0:
                heads += 1
        dict_heads[heads] = dict_heads.get(heads, 0) + 1
    for key, value in dict_heads.items():
        dict_heads[key] = value / 100
    return dict_heads
