import random


def flip_coin() -> dict:
    result_list = []
    for _ in range(10000):
        a, b = 0, 0
        for char in range(10):
            if random.randint(0, 1) == 0:
                a += 1
            else:
                b += 1
        result_list.extend([[a, b]])
    zero_ten = [0, 10]
    one_nine = [1, 9]
    two_eight = [2, 8]
    three_seven = [3, 7]
    four_six = [4, 6]
    five_five = [5, 5]
    ten_zero = [10, 0]
    nine_one = [9, 1]
    eight_two = [8, 2]
    seven_three = [7, 3]
    six_four = [6, 4]
    zero_ten_counter = result_list.count(zero_ten) / len(result_list) * 100
    one_nine_counter = result_list.count(one_nine) / len(result_list) * 100
    two_eight_counter = result_list.count(two_eight) / len(result_list) * 100
    three_seven_counter = (result_list.count(three_seven) / len(result_list)
                           * 100)
    four_six_counter = result_list.count(four_six) / len(result_list) * 100
    five_five_counter = result_list.count(five_five) / len(result_list) * 100
    six_four_counter = result_list.count(six_four) / len(result_list) * 100
    seven_three_counter = (result_list.count(seven_three) / len(result_list)
                           * 100)
    eight_two_counter = result_list.count(eight_two) / len(result_list) * 100
    nine_one_counter = result_list.count(nine_one) / len(result_list) * 100
    ten_zero_counter = result_list.count(ten_zero) / len(result_list) * 100
    return {
        0: zero_ten_counter,
        1: one_nine_counter,
        2: two_eight_counter,
        3: three_seven_counter,
        4: four_six_counter,
        5: five_five_counter,
        6: six_four_counter,
        7: seven_three_counter,
        8: eight_two_counter,
        9: nine_one_counter,
        10: ten_zero_counter
    }
