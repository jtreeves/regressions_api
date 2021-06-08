from matplotlib.figure import Figure
from numpy import arange

def create_hyperbolic_graph():
    fig = Figure()
    graph = fig.add_subplot(1, 1, 1)
    xs = arange(0.1, 10.0, 0.1)
    ys = [(2 / x + 3) for x in xs]
    graph.plot(xs, ys)
    graph.grid()
    return fig