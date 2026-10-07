import random


def flip_coin() -> dict[int, float]:
    cases = 10_000
    heads_counts = {heads: 0 for heads in range(11)}

    for _ in range(cases):
        heads = sum(random.choice((True, False)) for _ in range(10))
        heads_counts[heads] += 1

    return {
        heads: round(count / cases * 100, 2)
        for heads, count in heads_counts.items()
    }


def draw_gaussian_distribution_graph() -> None:
    import matplotlib.pyplot as plt

    distribution = flip_coin()
    plt.plot(distribution.keys(), distribution.values(), color="blue")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.xticks(range(11))
    plt.ylim(0, 100)
    plt.savefig("gaussian_distribution.png")
    plt.close()
