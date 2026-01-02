import random


def flip_coin(trials: int = 10000, flips: int = 10) -> dict:
    if not isinstance(trials, int) or trials <= 0:
        raise ValueError("Trials must be a positive integer")
    if not isinstance(flips, int) or flips <= 0:
        raise ValueError("Flips must be a positive integer")

    counts = {i: 0 for i in range(flips + 1)}
    for _ in range(trials):
        heads = sum(random.randint(0, 1) for _ in range(flips))
        counts[heads] += 1

    return {k: round((v / trials) * 100, 2) for k, v in counts.items()}


def draw_gaussian_distribution_graph(data: dict, max_width: int = 50) -> None:
    max_pct = max(data.values()) if data.values() else 1

    print("\nРозподіл результатів (масштабований ASCII графік):")
    for heads, percentage in data.items():
        bar_length = int((percentage / max_pct) * max_width)
        visual_bar = "█" * bar_length
        print(f"{heads:2}: {visual_bar} {percentage}%")


if __name__ == "__main__":
    stats = flip_coin(trials=10000, flips=10)
    print(stats)
    draw_gaussian_distribution_graph(stats)
