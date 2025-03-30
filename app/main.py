import random


def heads_count(numbers: int = 10) -> int:
    count = 0
    for i in range(numbers):
        if random.choice([0, 1]) == 0:
            count += 1
    return count


def flip_coin() -> dict:
    listt = []
    for num in range(10000):
        listt.append(heads_count())

    answer_dict = {
        number: listt.count(number) / 100 for number in range(0, 11)
    }
    return answer_dict
