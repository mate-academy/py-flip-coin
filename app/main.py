import random
import matplotlib as mpl
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {}
    for i in range(10000):
        cnt = 0
        for _ in range(10):
            if random.randint(0, 1):
                cnt += 1
        if cnt in result:
            result[cnt] += 1
        else:
            result[cnt] = 1
    res = sorted(result.items())
    sorted_dict = {}
    for key, value in res:
        sorted_dict[key] = (value / 100)
    return sorted_dict


def draw_gaussian_distribution_graph() -> None:
    gaussian_distribution = flip_coin()
    axis_y = []
    for key, value in gaussian_distribution.items():
        axis_y.append(gaussian_distribution[key])
    dpi = 80
    fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
    mpl.rcParams.update({"font.size": 14})
    plt.axis([0, 10, 0, 100])
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.xticks(range(len(gaussian_distribution)))
    plt.ylabel("Drop percentage %")
    plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    heads_count = range(len(gaussian_distribution))
    drop_percentage = axis_y
    plt.plot(heads_count, drop_percentage, color="blue", linestyle="solid",
             label="Gaussian distribution")
    fig.savefig("Gaussian distribution.png")


draw_gaussian_distribution_graph()
