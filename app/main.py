import random
# import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result_list = [sum(random.choice([0, 1])
                       for _ in range(10)) for _ in range(10000)]
    result_dict = {i: round(result_list.count(i) / 10000 * 100, 2)
                   for i in range(11)}
    return result_dict

# def draw_gaussian_distribution_graph(result_dict: dict) -> None:
#     x_param = list(result_dict.keys())
#     y_param = list(result_dict.values())
#     plt.figure(figsize=(10, 6))
#     plt.plot(x_param, y_param)
#     plt.yticks(range(0, 110, 10))
#     plt.title("Gaussian distribution")
#     plt.xlabel("Heads count")
#     plt.ylabel("Drop percentage %")
#     plt.show()
