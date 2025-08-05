import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    heads = 0
    tails = 0
    for _ in range(10):
        flip = random.randint(0, 1)
        if flip == 1:
            heads += 1
        else:
            tails += 1
    return {"heads": heads, "tails": tails}


results = {}
for _ in range(10000):
    res = flip_coin()
    heads_count = res["heads"]
    if heads_count in results:
        results[heads_count] += 1
    else:
        results[heads_count] = 1


def draw_gaussian_distribution_graph(results: dict) -> None:
    keys = sorted(results.keys())
    values = [results[k] for k in keys]
    plt.bar(keys, values, color="skyblue")

    plt.xlabel("Number of heads in 10 coin flips")
    plt.ylabel("Frequency")
    plt.title("Distribution of the number of eagles in 10,000 simulations")
    plt.show()


draw_gaussian_distribution_graph(results)
