from collections import Counter
import random
from typing import Dict


def flip_coin() -> Dict[int, float]:
    total_simulations: int = 10000
    num_flips: int = 10
    head_counts: Counter[int] = Counter()

    for _ in range(total_simulations):
        # Simula 10 tiradas y cuenta caras
        heads: int = sum(
            random.choice([0, 1]) for _ in range(num_flips)
        )
        head_counts[heads] += 1

    # Calcula el porcentaje para cada cantidad de caras del 0 al 10
    result: Dict[int, float] = {}
    for i in range(num_flips + 1):
        percentage: float = round(
            (head_counts[i] / total_simulations) * 100, 2
        )
        result[i] = percentage

    return result


if __name__ == "__main__":
    print(flip_coin())
