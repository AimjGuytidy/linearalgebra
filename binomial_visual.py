import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

N = 10
thetas = [0.25, 0.5, 0.75, 0.9]
x = np.arange(0, N + 1)


def make_graph(data):
    plt.figure()
    x = data["x"]
    n = data["n"]
    theta = data["theta"]

    probs = binom.pmf(x, n, theta)
    title = r"$\theta=" + str(theta) + "$"

    plt.bar(x, probs, align="center")
    plt.xlim([min(x) - 0.5, max(x) + 0.5])
    plt.ylim([0, 0.4])
    plt.xticks(x)
    plt.xlabel("$x$")
    plt.ylabel("$p(x)$")
    plt.title(title)
    sns.despine()
    plt.savefig("binomDistTheta" + str(int(theta * 100)) + ".pdf")


for theta in thetas:
    data = {"x": x, "n": N, "theta": theta}
    make_graph(data)
