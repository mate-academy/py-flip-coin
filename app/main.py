import random
import math


def flip_coin(num_experiments: int = 10000) -> dict[int, float]:
    results = {i: 0 for i in range(11)}

    for _ in range(num_experiments):
        heads = sum(random.randint(0, 1) for _ in range(10))
        results[heads] += 1

    for key in results:
        percent = results[key] * 100 / num_experiments
        results[key] = math.floor(percent * 100) / 100

    return results


if __name__ == "__main__":
    result = flip_coin()
    print("Розподіл кількості орлів в %:")
    for heads, percent in sorted(result.items()):
        print(f"{heads} орлів: {percent}%")
