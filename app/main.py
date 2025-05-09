import matplotlib.pyplot as plt


x = list(range(11))
y = [0, 1, 4, 12, 20, 25, 20, 12, 4, 1, 0]

plt.plot(x, y, color="blue")

plt.xlabel("Heads count")
plt.ylabel("Drop percentage %")
plt.title("Gaussian distribution")

plt.show()
