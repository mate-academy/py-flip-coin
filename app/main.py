import random


def flip_coin():
    result_question = []

    for _ in range(10000):
        coin_eagle = 0
        question_coin = (0, 1)
        for coin in range(10):
            coin_eagle += random.choice(question_coin)
        result_question.append(coin_eagle)

    return {i: result_question.count(i) * 100 / 10000 for i in range(11)}
