import matplotlib.pyplot as plt


def draw_distribution(percentages: dict) -> None:
    plt.bar(percentages.keys(), percentages.values())
    plt.title("Distribution of the number of heads in 10 coin flips")
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage of cases")
    plt.show()
