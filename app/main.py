import random


def head_or_tail_counter() -> dict:
    head = 0
    tail = 0
    for _ in range(10):
        if random.randint(0, 1) == 0:
            head += 1
        else:
            tail += 1
    percent_results = {"Heads": head / 10, "Tails": tail / 10}
    return {"Heads": head, "Tails": tail, "Percent Results": percent_results}


def flip_coin() -> dict:
    overall_score = {i: 0 for i in range(11)}
    for _ in range(10000):
        result = head_or_tail_counter()
        num_heads = result["Heads"]
        overall_score[num_heads] += 1
    return convert_to_percentage(overall_score)


def convert_to_percentage(score: dict) -> dict:
    total = sum(score.values())
    round_percents = {
        key: round(value / total * 100, 2) for key, value in score.items()
    }
    return round_percents
