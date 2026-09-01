from random import choice


def flip_coin() -> dict:
    coin = ["Heads", "Tails"]

    flip_dict = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads_counter = 0
        for flip in range(1, 11):
            if choice(coin) == "Heads":
                heads_counter += 1

        flip_dict[heads_counter] += 1

    flip_dict = {key: value / 10000 * 100 for key, value in flip_dict.items()}

    return flip_dict
