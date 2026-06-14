import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    main_dict = {}
    for cycle in range(10000):
        dict_inner = {}
        for tries in range(10):
            point = random.choice([0, 1])
            if point not in dict_inner:
                dict_inner[point] = 1
            else:
                dict_inner[point] += 1
        head_num = dict_inner.get(1, 0)
        if head_num not in main_dict:
            main_dict[head_num] = 1
        else:
            main_dict[head_num] += 1

    for key, value in main_dict.items():
        temp = value
        new_value = temp / 10000 * 100
        main_dict[key] = round(new_value, 2)

    sorted_dict = dict(sorted(main_dict.items()))
    return sorted_dict


def draw_gaussian_distribution_graph(sorted_dict: dict) -> None:

    y_vertical = [value for key, value in sorted_dict.items()]
    x_horizontal = [key for key, value in sorted_dict.items()]

    plt.plot(x_horizontal, y_vertical)

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
