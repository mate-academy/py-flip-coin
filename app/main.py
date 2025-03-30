import random
import decimal


def flip_coin() -> dict:
    coin = ["head", "tails"]
    n_of_iterations = 10000
    percent = decimal.Decimal("100") / decimal.Decimal(str(n_of_iterations))
    results_dict = {i: decimal.Decimal("0") for i in range(0, 11)}
    for _ in range(n_of_iterations):
        head_flip_counter = 0
        for _ in range(10):
            if random.choice(coin) == "head":
                head_flip_counter += 1
        results_dict[head_flip_counter] += percent

    results_dict = {key: float(value) for key, value in results_dict.items()}
    return results_dict
