import random

def flip_coin(n_cases=10000) -> None:
    results = {i: 0 for i in range(11)}  # 0..10 heads

    for _ in range(n_cases):
        heads = 0
        for _ in range(10):
            if random.random() < 0.5:
                heads += 1
        results[heads] += 1

    # convert to percentages
    for k in results:
        results[k] = round(results[k] / n_cases * 100, 2)

    return results


print(flip_coin())
