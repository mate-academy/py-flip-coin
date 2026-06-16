import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    resultados = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads_count = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                heads_count += 1
        resultados[heads_count] += 1

    for chave in resultados:
        resultados[chave] = (resultados[chave] / 10000) * 100

    return resultados


def draw_gaussian_distribution_graph() -> None:
    dados = flip_coin()

    eixo_x = list(dados.keys())
    eixo_y = list(dados.values())

    plt.bar(eixo_x, eixo_y)
    plt.show()
