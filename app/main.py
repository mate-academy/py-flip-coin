import random



def flip_coin():
    coin = ["heads", "tails"]
    counts = {k: 0 for k in range(11)}
    result_dict = {}
    total = 10000
    for i in range(total):
        heads_count = 0
        for j in range(10):
            random_choice = random.choice(coin)
            if random_choice == "heads":
                heads_count += 1
        counts[heads_count] += 1

    for k in range(11):
        percentage = counts[k] / total * 100
        rounded_percentage = round(percentage, 2)
        result_dict[k] = rounded_percentage

    print (result_dict)
    return result_dict

flip_coin()
