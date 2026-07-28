import random


import matplotlib.pyplot as plt


def flip_coin() -> dict:
    cases = 10000
    result = {heads: 0 for heads in range(11)}

    for _ in range(cases):
        heads = 0
        for _ in range(10):
            heads += random.randint(0, 1)

        result[heads] += 1

    for heads in result:
        result[heads] = round((result[heads] / cases * 100) , 2)

    return result


result = flip_coin()

fig, ax = plt.subplots()

ax.plot(result.keys(), result.values())

plt.show()
