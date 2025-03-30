import random


def flip_coin() -> dict:
    num_cases = 10000
    num_flips = 10
    results = {}

    for _ in range(num_cases):
        num_heads = 0
        for _ in range(num_flips):
            if random.random() < 0.5:
                num_heads += 1

        if num_heads in results:
            results[num_heads] += 1
        else:
            results[num_heads] = 1

    percentages = (
        {num_heads: (count / num_cases * 100)
         for num_heads, count in results.items()}
    )
    return percentages


def draw_gaussian_distribution_graph(show_case: dict[str, float]) -> None:
    import matplotlib.pyplot as plt

    heads = list(show_case.keys())
    percentages = list(show_case.values())

    plt.plot(heads, percentages)
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.title("Distribution of Number of Heads in 10 Coin Flips")
    plt.show()

# show_case = flip_coin()
# print(show_case)
# draw_gaussian_distribution_graph(show_case)
