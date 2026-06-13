import  random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    new_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
                6: 0, 7: 0, 8: 0, 9: 0, 10: 0}

    for _ in range(10000):
        heads = 0
        for _ in range(10):
            value = random.choice([0, 1])
            if value == 1:
                heads += 1
        new_dict[heads] += 1

    for key in new_dict:
        new_dict[key] = round((new_dict[key] / 10000) * 100, 2)
    return new_dict

def draw_gaussian_distribution_graph():
    data = flip_coin()
    x = list(data.keys())
    y = list(data.values())
    plt.plot(x, y)

    plt.title("Gaussian Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()

if __name__ == "__main__":
    draw_gaussian_distribution_graph()