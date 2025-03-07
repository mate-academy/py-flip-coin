from collections import OrderedDict
import random


def flip_coin() -> dict:
    count_all = dict()
    cases = 10000
    flips = 10
    for _ in range(cases):
        count_head = 0
        for _ in range(flips):
            if random.randint(0, 1) == 0:
                count_head += 1
        count_head_stat = count_all.get(count_head)
        if count_head_stat is None:
            count_all[count_head] = 1
        else:
            count_all[count_head] = count_head_stat + 1

    # xpoints = np.array([1, 8])
    # ypoints = np.array([3, 10])

    result = {heads: round(counter / cases * 100, 2)
              for heads, counter in count_all.items()}

    result_sorted = OrderedDict(sorted(result.items()))

    return result_sorted
