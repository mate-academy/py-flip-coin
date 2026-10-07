import random


def flip_coin() -> dict[int, float]:
    cases = 10_000
    counts = {heads: 0 for heads in range(11)}

    for _ in range(cases):
        heads_count = 0

        for _ in range(10):
            if random.choice(["Heads", "Tails"]) == "Heads":
                heads_count += 1

        counts[heads_count] += 1

    return {
        heads: count / cases * 100
        for heads, count in counts.items()
    }


print(flip_coin())
