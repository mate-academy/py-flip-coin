from __future__ import annotations

import random


class Experiment:
    times = 10

    def __init__(self) -> None:
        self.__heads = sum(
            random.choice([0, 1])
            for _ in range(self.times)
        )

    @property
    def heads_flipped(self) -> int:
        return self.__heads

    @classmethod
    def do_flips(cls, cases: int) -> dict:
        results = {heads: 0.00 for heads in range(cls.times + 1)}
        for _ in range(cases):
            results[cls().heads_flipped] += 1

        return results
