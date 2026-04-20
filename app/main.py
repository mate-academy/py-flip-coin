import random
# from matplotlib import pyplot


def flip_coin() -> dict:
    number_of_cases = 10_000
    percentage_of_each_case = 100 / number_of_cases

    drop_percentage = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }

    for _ in range(number_of_cases):
        number_of_heads = 0
        for _ in range(10):
            if random.choice(["head", "tail"]) == "head":
                number_of_heads += 1

        drop_percentage[number_of_heads] += percentage_of_each_case

    return drop_percentage


# def draw_gaussian_distribution_graph(drop_percentage: dict) -> None:
#     x_coordinate = list(drop_percentage.keys())
#     y_coordinate = list(drop_percentage.values())
#
#     pyplot.plot(x_coordinate, y_coordinate)
#     pyplot.xlabel("Heads count")
#     pyplot.ylabel("Drop percentage %")
#     pyplot.title("Guassian distribution")
#
#     pyplot.show()
