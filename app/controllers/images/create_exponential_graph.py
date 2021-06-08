from matplotlib.figure import Figure
from numpy import arange

def create_exponential_graph():
    fig = Figure(figsize=(5, 5))
    fig.set_tight_layout(True)
    graph = fig.add_subplot(1, 1, 1)
    xs = arange(0.0, 10.0, 0.1)
    ys = [(2 * 3**x) for x in xs]
    graph.plot(xs, ys)
    graph.grid()
    return fig