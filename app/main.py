import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    total_trials = 10000
    flips_per_trial = 10
    results = {i: 0 for i in range(flips_per_trial + 1)}

    for _ in range(total_trials):
        heads_count = sum(random.random() < 0.5 for _ in range(flips_per_trial))
        results[heads_count] += 1

    # Converte contagem absoluta para porcentagem
    return {
        key: (value / total_trials) * 100 
        for key, value in results.items()
    }


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    
    x_values = list(data.keys())
    y_values = list(data.values())

    plt.plot(x_values, y_values, marker="o")
    plt.title("Gaussian Distribution of Coin Flips")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # Exemplo de saída do dicionário
    print(flip_coin())
    # Chama a função para desenhar o gráfico
    draw_gaussian_distribution_graph()
