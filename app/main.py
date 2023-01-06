from random import choice


def flip_coin() -> dict:
    val_nul = {num: 0 for num in range(11)}
    for num in range(10000):
        number = 0
        for _ in range(10):
            if choice(["Hed", "Teil"]) == "Hed":
                number += 1
        val_nul[number] += 1
    for i in val_nul:
        val_nul[i] /= 100
    return val_nul


if __name__ == "__main__":
    print(flip_coin())
