import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom


def binomialGraph(n: int, p: float, k: int = None) -> None:
    """
    A function that generates a binomial graph based on the given parameters.

    Parameters:
    - n (int): the number of trials in the binomial distribution.
    - p (float): the probability of success in each trial.

    Returns:
    - None
    """
    x: list = np.arange(0, n + 1)
    binomial: list = binom.pmf(k=x, n=n, p=p)

    plt.bar(x, binomial)

    if k != None:
        y_point: float = binomial[k]
        plt.stem(k, y_point, markerfmt="ro", label=f"P(X = {k}) = {y_point}")

    plt.xlabel("x", fontsize=12)
    plt.legend()
    plt.ylabel("Probabilidade", fontsize=12)
    plt.xlim([-1, n + 1])
    plt.title("Distribuição Binomial, n={0}, p={1}".format(n, p), fontsize=15)
    plt.show()

    return


if __name__ == "__main__":
    n: int = 50
    p: float = 0.50
    k: int | None = None
    binomialGraph(n, p, k)
