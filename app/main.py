from random import randint


def flip_coin() -> dict:
    results = {heads: 0 for heads in range(11)}
    total_trials = 10000

    for _ in range(total_trials):
        count_heads = 0
        for _ in range(10):
            flip = randint(0, 1)
            if flip == 1:
                count_heads += 1
        results[count_heads] += 1

    results = {
        key: (result / total_trials) * 100
        for key, result in results.items()
    }

    return results
