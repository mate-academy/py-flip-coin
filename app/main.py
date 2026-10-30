import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result_dict = {}
    for _ in range(10000):

        toss_list = []
        for _ in range(10):
            toss_list.append(random.randint(0, 1))

        heads_numbers = toss_list.count(1)
        result_dict[heads_numbers] = result_dict.get(heads_numbers, 0) + 1

    for key, value in result_dict.items():
        result_dict[key] = round((value / 100), 2)
    return result_dict


def draw_gaussian_distribution_graph(result_dict: dict) -> None:
    plt.bar((list(result_dict.keys())), (list(result_dict.values())))

    plt.xlabel("Кількість орлів (з 10 кидків)")
    plt.ylabel("Відсоток випадіння (%)")
    plt.title("Симуляція підкидання монети (10 000 експериментів)")

    plt.show()
