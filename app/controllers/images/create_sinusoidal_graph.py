from matplotlib.figure import Figure
from numpy import arange, sin, pi

def create_sinusoidal_graph():
    fig = Figure()
    graph = fig.add_subplot(1, 1, 1)
    xs = arange(0.0, 10.0, 0.1)
    ys = [(5 * sin(2 * (x - 3)) + 7) for x in xs]
    graph.plot(xs, ys)
    graph.grid()
    return fig