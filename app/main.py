import random

def flip_coin() -> None:
    how_many = 0
    coin = random.randint(0, 1)
    if coin == 1:
        how_many += 1
    print(how_many)

flip_coin()