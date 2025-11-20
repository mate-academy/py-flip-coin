import matplotlib.pyplot as plt
from app.main import flip_coin
from typing import Dict


def flip_coin_and_draw(trials: int = 10000) -> Dict[int, float]:
    results = flip_coin(trials)

    keys = list(results.keys())
    values = [results[k] for k in keys]

    plt.figure(figsize=(10, 5))
    plt.plot(keys, values, marker="o")
    plt.title("Distribution of Heads in 10 Coin Flips")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.grid(True)
    plt.show()

    return results
