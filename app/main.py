import random
# import matplotlib.pyplot as plt


def flip_coin() -> dict:
    coin = ["Head", "Eagle"]
    result = {key: 0 for key in range(11)}

    for _ in range(10000):
        heads = 0
        eagles = 0
        for i in range(10):
            flip = random.choice(coin)
            if flip == "Head":
                heads += 1
            else:
                eagles += 1
        result[heads] += 1

    for key, value in result.items():
        result[key] = round(value / 10000 * 100, 2)

    return result


# result = flip_coin()
#
# xpoints = result.keys()
# ypoints = result.values()
#
# plt.plot(xpoints, ypoints)
# plt.ylim(0, 100)
# plt.title("Gaussian distribution")
# plt.xlabel("count of heads")
# plt.ylabel("Percent")
# plt.show()
