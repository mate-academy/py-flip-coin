import random


def flip_coin() -> None:
    experiment_data = {}
    case_amount = 10000
    list_of_heads = []

    for i in range(case_amount):
        heads10 = 0

        for _ in range(10):
            # flip = random.randint(0, 1)
            flip = round(random.random())
            if flip == 0:
                heads10 += 1
        list_of_heads.append(heads10)

    for head_res in list_of_heads:
        if head_res not in experiment_data:
            experiment_data[head_res] = (
                round(
                    list_of_heads.count(head_res) / 100,
                    2
                )
            )
    experiment_data = dict(sorted(experiment_data.items()))
    return experiment_data
