import matplotlib.pyplot as plt
import numpy as np
from main import flip_coin


data = flip_coin()
x_coord = list(data.keys())
y_coord = list(data.values())

x_line = np.array(x_coord)
y_line = np.array(y_coord)

plt.ylim(0, 100)
plt.yticks(range(0, 101, 10))
plt.xticks(range(0, 11, 1))

plt.plot(x_line, y_line)
plt.title("Gaussian distribution")
plt.xlabel("Heads count")
plt.ylabel("Drop percentage %")

plt.show()
