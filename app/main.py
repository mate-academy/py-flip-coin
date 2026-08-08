import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    # Aumentar ligeramente el número de casos mejora la precisión
    # y reduce la desviación estándar de la simulación.
    trials = 10000
    counts = {i: 0 for i in range(11)}

    for _ in range(trials):
        heads = 0
        for _ in range(10):
            if random.random() < 0.5:
                heads += 1
        counts[heads] += 1

    # Calculamos el porcentaje exacto
    return {k: (v / trials) * 100 for k, v in counts.items()}


def draw_gaussian_distribution_graph(data: dict[int, float]) -> None:
    # Preparamos los datos para el gráfico
    x_values = list(data.keys())
    y_values = list(data.values())

    plt.plot(x_values, y_values, marker="o")

    # Añadimos etiquetas y título
    plt.title("Coin Toss Gaussian Distribution")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.grid(True)

    plt.show()
