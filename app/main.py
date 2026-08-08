import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {}
    for _ in range(100000):
        heads = 0
        for _ in range(10):
            random_coin = random.choice([True, False])
            if random_coin:
                heads += 1
        result[heads] = result.get(heads, 0) + 1
    for i in range(11):
        result.setdefault(i, 0)

    total = sum(result.values())
    percentage = {key: round((value / total) * 100, 2)
                  for key, value in result.items()}
    sorted_result = dict(sorted(percentage.items()))
    return sorted_result


data = flip_coin()
x_axis = data.keys()
y_axis = data.values()
plt.plot(x_axis, y_axis)
plt.xlim(0, 10)
plt.ylim(0, 100)
plt.xlabel("Heads count")
plt.ylabel("Drop percentage %")
plt.show()
