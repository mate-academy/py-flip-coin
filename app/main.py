import random
# import sys
# import matplotlib.pyplot as plt


def flip_coin(sets: int = 10000) -> dict:
    drops_set = {}

    def drop_ten() -> int:
        rez = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                rez += 1
        return rez
    for i in range(sets):
        drops_set[i] = drop_ten()
    result = {}
    for i in range(11):
        result[i] = ((list(drops_set.values()).count(i)) / len(
            drops_set)) * 100
    print(result)
    return result


# def draw_gaussian_distribution_graph() -> None:
#     flips = flip_coin(10000)
#     xpoints = list(flips.keys())
#     ypoints = list(flips.values())
#     plt.plot(xpoints, ypoints)
#     plt.xlabel("Value")
#     plt.ylabel("Number of falls")
#     plt.show()
#     plt.savefig(sys.stdout.buffer)
#     sys.stdout.flush()
