import random
import matplotlib.pyplot as plt


def flip_coin(flip: int = 10000) -> dict:
    result = {i: 0 for i in range(11)}
    for i in range(flip):
        count_heads = sum(random.randint(0, 1) for _ in range(10))
        result[count_heads] += 1
    for count in result:
        result[count] = (result[count] / flip) * 100
    return result


def draw_gaussian_distribution_graph(result: dict) -> None:
    counts = list(result.keys())
    percentages = list(result.values())
    plt.figure(figsize=(10, 6))
    plt.bar(counts, percentages, color="skyblue", edgecolor="black")



# write your code here
