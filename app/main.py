import random


def flip_ten_times() -> int:
    heads_count = 0
    for _ in range(10):
        if random.randint(0, 1) == 0:  # 0 = cara
            heads_count += 1
    return heads_count


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads = flip_ten_times()
        results[heads] += 1

    percentages = {}
    for key, value in results.items():
        percentages[key] = round((value / 10000) * 100, 2)

    return percentages


if __name__ == "__main__":
    print(flip_coin())
