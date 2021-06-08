from matplotlib.figure import Figure
from numpy import arange, sin, pi

def create_sin_graph():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = arange(0.0, 2.0, 0.01)
    ys = [(1 + sin(2 * pi * x)) for x in xs]
    axis.plot(xs, ys)
    axis.plot([1], [1], marker='o', markersize=3, mfc='none', color="red")
    return fig