import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result_dict: dict = {i: 0.0 for i in range(11)}
    random_number_of_tests = random.randint(10000, 10500)
    for _ in range(random_number_of_tests):
        num_of_heads = 0
        for _ in range(10):
            head_or_tails = random.randint(0, 1)
            num_of_heads += head_or_tails

        result_dict[num_of_heads] += 1

    for i in range(11):
        result_dict[i] = round(
            result_dict[i] / random_number_of_tests * 100,
            2
        )

    return result_dict


def draw_gaussian_distribution_graph() -> None:
    results = flip_coin()

    x_results = list(results.keys())
    y_results = list(results.values())

    plt.plot(x_results, y_results)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
