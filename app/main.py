import random


def flip_coin() -> dict:
    final_dict = {}
    toss_results = []

    for _ in range(0, 10000):
        toss = []
        for _ in range(10):
            coin_status = random.randint(1, 2)
            if coin_status == 1:
                toss.append("heads")
            else:
                toss.append("tails")
        toss_results.append(toss)

    for result in toss_results:
        heads_count = result.count("heads")
        if heads_count not in final_dict:
            final_dict[heads_count] = 0
        final_dict[heads_count] += 1 / 100

    for key in final_dict:
        final_dict[key] = round(final_dict[key], 2)

    return final_dict
