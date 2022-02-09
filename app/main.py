from random import randint

import matplotlib.pyplot as plt


def flip_coin():
    flips_result = {item: 0 for item in range(11)}

    for _ in range(10000):
        heads = sum(randint(0, 1) for _ in range(10))
        flips_result[heads] += 1

    flips_result = {flip: round(count * 100 / 10000, 2)
                    for flip, count in flips_result.items()}

    return flips_result


def create_graph():
    data = flip_coin()
    plt.axis([0, 10, 0, 100])
    plt.title('Gaussian distribution')
    plt.xlabel('Heads count')
    plt.ylabel('Drop percentage %')
    plt.plot(data.keys(), data.values())
    plt.show()


if __name__ == "__main__":
    create_graph()
