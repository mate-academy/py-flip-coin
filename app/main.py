import random
# import matplotlib.pyplot as plt


def flip_coin(
        number_of_simulations: int = 10000,
        number_of_tosses: int = 10
) -> dict:
    result_dict = {number_of_heads: 0 for number_of_heads
                   in range(number_of_tosses + 1)}
    for _ in range(number_of_simulations):
        case_result = [random.choice(["Head", "Tail"]) for _
                       in range(number_of_tosses)]
        result_dict[case_result.count("Head")] += 1
    for number_of_heads in result_dict:
        result_dict[number_of_heads] = (
            (result_dict[number_of_heads] / number_of_simulations) * 100
        )
    return result_dict


# def draw_gaussian_distribution_graph() -> None:
#     x_points = list(flip_coin().keys())
#     y_points = list(flip_coin().values())
#     plt.plot(x_points, y_points)
#     plt.xlabel("Heads count")
#     plt.ylabel("Drop percentage %")
#     plt.show()
