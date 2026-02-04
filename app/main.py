# write your code here
import random
from collections import defaultdict

def flip_coin(num_flips: int = 10, num_trials: int = 10000) -> dict[int, float]:
    counts = defaultdict(int)

    for _ in range(num_trials):
        heads = sum(random.choice([0, 1]) for _ in range(num_flips))
        counts[heads] += 1

    # Перетворюємо в відсотки
    percentages = {k: round(v / num_trials * 100, 2) for k, v in counts.items()}
    # Додаємо нулі, якщо якісь значення відсутні
    for i in range(num_flips + 1):
        if i not in percentages:
            percentages[i] = 0.0

    # Сортуємо по ключу
    return dict(sorted(percentages.items()))
