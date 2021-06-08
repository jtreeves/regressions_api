from matplotlib.figure import Figure
from numpy import arange

def create_minimum_graph():
    fig = Figure()
    graph = fig.add_subplot(1, 1, 1)
    xs = arange(0.0, 10.0, 0.1)
    ys = [(x**3 - 15 * x**2 + 63 * x - 31) for x in xs]
    graph.plot(xs, ys)
    graph.plot([7], [18], marker='o', markersize=10, mfc='none', color='red')
    graph.grid()
    return fig