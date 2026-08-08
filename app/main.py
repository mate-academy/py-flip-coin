import random

# import seaborn as sns
# import matplotlib.pyplot as plt


def flip_coin(cases: int = 10000) -> dict:

    result = {tries: 0 for tries in range(11)}

    for _ in range(cases):
        count = sum(random.choice([1, 0]) for _ in range(10))
        result[count] += (1 / cases) * 100
    return result

#
# def draw_gaussian_distribution_graph():
#
#     data = flip_coin()
#
#     sns.barplot(x=list(data.keys()), y=list(data.values()))
#
#     plt.xlabel("Tries")
#     plt.ylabel("Probability")
#
#     plt.show()
