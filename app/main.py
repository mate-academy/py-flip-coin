import random


def flip_coin() -> dict:
    number_of_tests = 10000
    events = ["H", "T"]
    res = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for _ in range(number_of_tests):
        one_test_log = []
        for _ in range(10):
            one_test_log.append(random.choice(events))
            one_test_log.count("H")
        res[one_test_log.count("H")] += 1

    for key, value in res.items():
        res[key] = round((value * 100 / number_of_tests), 2)

    return res


def draw_gaussian_distribution_graph(results: dict) -> None:
    pass


if __name__ == "__main__":
    flip_coin()
