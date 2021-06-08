from matplotlib.figure import Figure
from numpy import arange, exp

def create_logistic_graph():
    fig = Figure()
    graph = fig.add_subplot(1, 1, 1)
    xs = arange(0.0, 10.0, 0.1)
    ys = [(2 / (1 + exp(-3 * (x - 5)))) for x in xs]
    graph.plot(xs, ys)
    graph.grid()
    return fig