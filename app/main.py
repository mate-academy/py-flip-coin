import random


def flip_coin() -> dict:
    coin = ["head", "tails"]
    heads_dropped = {}
    for times in range(11):
        head_times_appear = 0
        for flip in range(10000):
            count_heads = sum(1 for _ in range(10)
                              if random.choice(coin) == "head")
            if count_heads == times:
                head_times_appear += 1
        percentage = 100 * (head_times_appear / 10000)
        heads_dropped[times] = percentage
    return heads_dropped
