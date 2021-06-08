from matplotlib.figure import Figure
from numpy import arange

def create_quadratic_graph():
    fig = Figure(figsize=(5, 5))
    fig.set_tight_layout(True)
    graph = fig.add_subplot(1, 1, 1)
    xs = arange(0.0, 10.0, 0.1)
    ys = [(x**2 - 12 * x + 66) for x in xs]
    graph.plot(xs, ys)
    graph.grid()
    return fig