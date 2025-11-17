import random
from collections import Counter


def flip_coin(trials: int = 10000) -> dict:
    counts = Counter()

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(10))  # 0 = tails, 1 = heads
        counts[heads] += 1

    # Переводимо у відсотки
    percentages = {k: round(v / trials * 100, 2) for k, v in counts.items()}

    # Додаємо нулі для відсутніх варіантів (0..10)
    for i in range(11):
        percentages.setdefault(i, 0.0)

    # Сортуємо за ключами
    return dict(sorted(percentages.items()))


