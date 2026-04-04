import random


# write your code here

def flip_coin() -> dict:
    dictionary = {x: 0 for x in range(11)}
    for i in range(30000):
        total_heads = 0
        for flip_number in range(10):
            total_heads += random.randint(0, 1)
        dictionary[total_heads] += 1
    return {key: round((value / 30000), 3) * 100 for key, value in
            dictionary.items()}
