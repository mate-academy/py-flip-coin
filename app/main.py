import random
from matplotlib import pyplot as plt


def flip_coin() -> dict:
    count = {}
    for check1 in range(10000):
        front = 0
        for check2 in range(10):
            rand = random.randint(0, 1)
            if rand == 1:
                front += 1
        if count.get(front):
            count[front] = count[front] + 1
        else:
            count[front] = 1
    for check3 in count:
        count[check3] = count[check3] * 100 / 10000

    return count


def draw_gaussian_distribution_graph() -> None:
    func = flip_coin()
    way_x = [func[check] for check in sorted(func)]
    way_y = sorted(func)
    plt.plot(way_y, way_x)
    plt.show()
