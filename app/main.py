from random import randint
# import matplotlib.pyplot as plt


def flip_coin() -> dict:
    dict_ = {i: 0 for i in range(11)}
    for _ in range(10_000):
        heads = 0
        for _ in range(10):
            number = randint(0, 1)
            if number == 1:
                heads += 1
        dict_[heads] += 1
    for i in dict_:
        dict_[i] = round(dict_[i] / 10_000 * 100, 2)
    return dict_


# def draw_gaussian_distribution_graph(dict_: dict) -> None:
#     plt.figure(figsize=(10, 8))
#     plt.xlim(0, 10)
#     plt.ylim(0, 100)
#     plt.xticks(range(11))
#     plt.yticks(range(0, 101, 10))
#     plt.plot(dict_.keys(), dict_.values())
#     plt.title("Gaussian distribution")
#     plt.xlabel("Heads count")
#     plt.ylabel("Drop percentage %")
#     plt.show()
