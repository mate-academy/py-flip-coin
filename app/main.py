import random


def flip_coin() -> dict:
    result = {}
    luck = ["top", "bottom"]
    for i in range(11):
        result[i] = 0

    for _ in range(10000):
        tops_count = 0
        for _ in range(10):
            if random.choice(luck) == "top":
                tops_count += 1
        result[tops_count] += 1

    for key in result:
        result[key] = (result[key] * 100 / 10000)
    return result

flip_coin()

# If you flip a coin, heads will come up 50% of the time. But if you flip a coin 10 times, 
# what is the chance that heads will come up 5 times? 2 times?

# Write flip_coin function, that conducts at least 10000 cases of flipping a coin 10 times. 
# It should return dict, where keys are numbers of possible heads dropped (0 to 10), 
# and values are percentage of how many that number of heads dropped out of all cases.

# print(flip_coin())
# # {0: 0.13, 1: 0.97, 2: 4.22, 3: 12.04, ... }
# If you have done all correctly, you should note that the biggest percentage of a number of heads dropped is about the middle, 
# 4-6 times and tends to 0 when it is about the edges 0-1 and 9-10. It calls normal distribution or Gaussian distribution.

# Extra
# Write draw_gaussian_distribution_graph function, that draws a graph that shows the distribution.

# matplotlib is relevant library for this purpose.

# matplotlib, Plotting
# matplotlib, Labels