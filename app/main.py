from random import randint

from matplotlib import pyplot as plt


def flip_coin() -> dict:
    result_dict = {}

    number_of_cases = 10000

    for case in range(number_of_cases):
        number_of_heads = 0

        for flip in range(10):
            if randint(0, 1) == 0:
                number_of_heads += 1

        if number_of_heads in result_dict:
            result_dict[number_of_heads] += 100 / number_of_cases
        else:
            result_dict[number_of_heads] = 100 / number_of_cases
    return result_dict


def draw_gaussian_distribution_graph() -> None:
    plt.title("Gaussian distribution")
    plt.ylabel("Drop percentage %")
    plt.xlabel("Heads count")

    plt.axis(0, 10, 0, 100)

    x_list = [x for x in range(11)]
    y_list = []
    flip_result = flip_coin()
    for number in range(11):
        y_list.append(flip_result[number])

    plt.plot(x_list, y_list)

    plt.show()
