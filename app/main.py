import random


def flip_coin() -> dict[int, float]:
    trials = 100_000
    counts = {heads: 0 for heads in range(11)}
    for _ in range(trials):
        heads = random.getrandbits(10).bit_count()
        counts[heads] += 1
    return {heads: count * 100 / trials for heads, count in counts.items()}


def draw_gaussian_distribution_graph(
    file_name: str = "coin_distribution.png"
) -> None:
    import matplotlib.pyplot as plt

    distribution = flip_coin()
    figure, axis = plt.subplots()
    axis.bar(distribution.keys(), distribution.values(), color="#2563eb")
    axis.set(
        title="Heads in 10 fair coin flips",
        xlabel="Number of heads",
        ylabel="Percentage of trials",
        xticks=range(11),
    )
    figure.tight_layout()
    figure.savefig(file_name, dpi=180)
    plt.close(figure)
