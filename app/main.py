import random


def flip_coin(num_cases: int = 10000) -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(num_cases):
        heads_count = sum(random.randint(0, 1) for _ in range(10))
        results[heads_count] += 1

    # Calculate percentages
    total_cases = num_cases
    for heads, count in results.items():
        results[heads] = (count / total_cases) * 100

    return results


# Example usage
if __name__ == "__main__":
    coin_stats = flip_coin()
    print(coin_stats)
