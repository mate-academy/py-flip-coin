import random


def flip_coin() -> dict:
    result = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    
    for _ in range(10000):
        head = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                head += 1
        result[head] += 1
        
    final_result = {}
    for key in result:
        final_result[key] = (result[key] / 10000) * 100
        
    return final_result
