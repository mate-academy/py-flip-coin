import random


def flip_coin(num_flips: int = 10000, num_coin_tosses: int = 10) -> dict:
    results = {}

    for _ in range(num_flips):
        heads_count = sum(random.choice([0, 1]) for _ in range
                          (num_coin_tosses))
        results[heads_count] = results.get(heads_count, 0) + 1

    percentages = {heads: count / num_flips * 100 for heads,
                   count in results.items()}
    return percentages


def save_distribution_data(percentages: dict,
                           filename: str = "coin_toss_distribution.txt"
                           ) -> None:
    with open(filename, "w") as file:
        for heads, count in percentages.items():
            file.write(f"{heads}: {count}\n")


if __name__ == "__main__":
    results = flip_coin()
    print(results)

    save_distribution_data(results)
