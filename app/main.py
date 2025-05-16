import random
from collections import defaultdict

def flip_coin(trials=10000):
    results = defaultdict(int)

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        results[heads] += 1


    percentages = {i: round((results[i] / trials) * 100, 2) for i in range(11)}
    return percentages
print(flip_coin())