import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    main_result = {i: 0 for i in range(11)}
    flip_results = [random.choices([0, 1], k=10) for i in range(10000)]

    sum_of_flip_result = []

    for index_of_flip in range(len(flip_results)):
        sum_of_flip_result.append(
            sum(flip_results[index_of_flip])
        )

    for key in main_result.keys():
        main_result[key] = round(
            sum([1
                 for item in sum_of_flip_result
                 if item == key])
            / 10000 * 100,
            2
        )

    return main_result


def draw_gaussian_distribution_graph() -> None:
    draw_date = flip_coin()
    x_axis = list(draw_date.keys())
    y_axis = list(draw_date.values())
    plt.plot(x_axis, y_axis)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage, %")
