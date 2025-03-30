from random import choice


def flip_coin() -> dict:
    head, tail = 1, 0
    tosses, trials = 10, 10000
    counts = {}
    for _ in range(trials):
        count = 0
        for _ in range(tosses):
            side = choice((head, tail))
            if side == head:
                count += 1
        if count not in counts:
            counts[count] = 0
        counts[count] += 1
    keys = sorted(counts.keys())
    return {
        index: round(((counts[index] / trials) * 100), 2)
        for index in keys
    }
