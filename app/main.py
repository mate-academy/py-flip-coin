import random
import matplotlib.pyplot as plt


def flip_coin():
    cases = 10000
    flips = 10

    flip_dict = {i: 0 for i in range(0, 11)}

    for _ in range(cases):
        eagle_and_tails = {1: 0, 0: 0}  # 1 is head, 0 is heads dropped out

        for _ in range(flips):
            flip = random.randint(0, 1)
            eagle_and_tails[flip] += 1

        flip_dict[eagle_and_tails[1]] += 1

    for key in flip_dict.keys():
        flip_dict[key] = int(100 * (flip_dict[key] / cases))

    return flip_dict


def draw_gaussian_distribution_graph():
    datas = flip_coin()
    fig, ax = plt.subplots()

    ax.set_title("Gaussian distribution", fontsize=16)
    ax.set_ylabel("Drop percentage %")
    ax.set_xlabel("Heads count")
    ax.plot(datas.keys(), datas.values(), color=(1.0, 0.2, 0.3))

    plt.ylim([0, 100])
    plt.xlim([0, 10])
    plt.show()


if __name__ == "__main__":
    draw_gaussian_distribution_graph()
