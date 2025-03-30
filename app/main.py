import random


def flip_coin() -> dict:
    result = []

    for _ in range(10000):
        current_drop = 0
        for i in range(10):
            choice = random.choice(["head", "back"])
            if choice == "head":
                current_drop += 1
        result.append(current_drop)

    return {
        0: round(result.count(0) / len(result) * 100, 2),
        1: round(result.count(1) / len(result) * 100, 2),
        2: round(result.count(2) / len(result) * 100, 2),
        3: round(result.count(3) / len(result) * 100, 2),
        4: round(result.count(4) / len(result) * 100, 2),
        5: round(result.count(5) / len(result) * 100, 2),
        6: round(result.count(6) / len(result) * 100, 2),
        7: round(result.count(7) / len(result) * 100, 2),
        8: round(result.count(8) / len(result) * 100, 2),
        9: round(result.count(9) / len(result) * 100, 2),
        10: round(result.count(10) / len(result) * 100, 2),
    }
