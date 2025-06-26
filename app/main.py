from matplotlib import pyplot as plt
import random


coin_sides = ["Heads", "Tails"]
def flip_coin(n_trials: int = 10000, n_flips: int = 10) -> dict:
    result_dict = {}
    for _ in range(n_trials):
        counter = 0
        for _ in range(n_flips):
            choice = random.choice(coin_sides)
            if choice == coin_sides[0]:
                counter += 1
        result_dict[counter] = result_dict.get(counter, 0) + 1
    for key, value in enumerate(result_dict):
        result_dict[key] = round(result_dict[key]/n_trials * 100, 2)
    return dict(sorted(result_dict.items()))

def draw_gaussian_distribution_graph(result_dict: dict) -> None:
    x = list(result_dict.keys())
    y = list(result_dict.values())

    plt.plot(x, y)
    plt.ylim(0,100)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage%")
    plt.title("Gaussian distribution")
    plt.show()
