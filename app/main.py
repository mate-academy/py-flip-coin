import numpy as np


def flip_coin() -> dict:
    flips = list(np.random.binomial(n=10, p=0.5, size=10000))
    return dict(zip([i for i in range(11)], [(np.equal(flips, i).sum() * 100)
                                             / 10000 for i in range(11)]))
