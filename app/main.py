# write your code here
from collections import defaultdict
import random


def flip_coin() -> dict:

    # erstelle das Dictionary
    zehner_ergebnisse = defaultdict(int)
    final_ergebnisse = {}
    # erstelle die Münze
    münze = ["Kopf", "Zahl"]
    # simuliere den Münzwurf
    for _ in range(10000):
        wurf = [random.choice(münze) for _ in range(10)]
        # zähle die Ergebnisse
        anzahl = wurf.count("Kopf")
        zehner_ergebnisse[anzahl] += 1
    # berechne die Wahrscheinlichkeiten
    for anzahl, count in zehner_ergebnisse.items():
        wahrscheinlichkeit = round(((count / 10000) * 100), 2)
        final_ergebnisse[anzahl] = wahrscheinlichkeit
    # sortiere die Ergebnisse
    final_ergebnisse = dict(sorted(final_ergebnisse.items()))
    return final_ergebnisse


if __name__ == "__main__":
    print(flip_coin())
