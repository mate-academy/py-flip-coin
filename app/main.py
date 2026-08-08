import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    number_of_flips = 10
    possible_result = ["heads", "tails"]
    head_result = {i: 0 for i in range(11)}

    number_of_cycles = 10000

    for i in range(number_of_cycles):

        heads_count = 0

        for i in range(number_of_flips):

            result = random.choice(possible_result)
            if result == "heads":
                heads_count += 1

        head_result[heads_count] += 1

    head_result_share = {k: round(v / number_of_cycles * 100, 2) for k,
                         v in head_result.items()}
    return head_result_share


final_result = flip_coin()
print(final_result)

x_values = sorted(final_result.keys())
y_values = [final_result[k] for k in x_values]
plt.plot(x_values, y_values)
plt.xlabel("Number of heads")
plt.xlabel("Percentage (%)")
plt.title("Distribution of heads in 10 coin flips")
plt.ylim(0, 100)
plt.show()
