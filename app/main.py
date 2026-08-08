import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    """Подбрасывает монету 10 раз, повторяет эксперимент 10000 раз
    и возвращает словарь с процентом выпадений орлов от 0 до 10.
    """
    result = {i: 0 for i in range(11)}

    for _ in range(10000):
        eagle_count = 0
        for _ in range(10):
            throw = random.randint(0, 1)
            if throw == 1:
                eagle_count += 1
        result[eagle_count] += 1

    for key in result:
        result[key] = round((result[key] / 10000) * 100, 2)

    return result


def graphic_flip_coin() -> None:
    """Строит график распределения выпадений орлов при 10 бросках."""
    data = flip_coin()
    counts = list(data.keys())
    percentages = list(data.values())

    plt.bar(counts, percentages, color="skyblue", edgecolor="black")
    plt.xlabel("Количество орлов")
    plt.ylabel("Процент случаев")
    plt.title("Распределение выпадений орлов при 10 бросках")

    for index, value in enumerate(percentages):
        plt.text(index, value + 0.5, str(value), ha="center")

    plt.show()


if __name__ == "__main__":
    graphic_flip_coin()
