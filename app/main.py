import random


def flip_coin() -> dict[int, float]:
    n_trials = 10000
    n_flips = 10
    # Ініціалізуємо 0.0, щоб PyCharm знав, що тут будуть float
    results = {i: 0.0 for i in range(n_flips + 1)}

    for _ in range(n_trials):
        heads_count = sum(random.randint(0, 1) for _ in range(n_flips))
        # Додаємо 1.0 (float) до лічильника
        results[heads_count] += 1.0

    for heads in results:
        # Тепер тут float ділиться на int і множиться на int — все чітко
        results[heads] = (results[heads] / n_trials) * 100

    return results
