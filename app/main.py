import random
import matplotlib.pyplot as plt


def flip_coin(flip: int = 10000) -> dict:
    cases = ("orzeł", "reszka")
    distribution = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0,
                    5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for case in range(flip):
        results = []
        for i in range(10):
            results.append(random.choice(cases))

        head = results.count("orzeł")
        distribution[head] += 1

    for key in distribution:
        distribution[key] = (distribution[key] / flip) * 100
    return distribution


def draw_gaussian_distribution_graph(data: dict) -> None:
    heads_count = list(data.keys())
    percentages = list(data.values())

    plt.bar(heads_count, percentages)
    plt.xlabel("Liczba orłów w 10 rzutach")
    plt.ylabel("Procent wystąpień")
    plt.title("Rozkład wyników rzutu monetą (10 rzutów)")
    plt.show()


result = flip_coin()
draw_gaussian_distribution_graph(result)
