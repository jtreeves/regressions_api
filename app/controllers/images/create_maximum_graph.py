from matplotlib.figure import Figure
from numpy import arange

def create_maximum_graph():
    """ Use Matplotlib to create cubic graph with marked maximum point """

    # Create initial figure
    fig = Figure(figsize=(5, 5))
    fig.set_tight_layout(True)
    graph = fig.add_subplot(1, 1, 1)

    # Create range of x-values
    xs = arange(0.0, 10.0, 0.1)

    # Use x-values to generate y-values
    ys = [(x**3 - 15 * x**2 + 63 * x - 31) for x in xs]

    # Graph points, and mark maximum point
    graph.plot(xs, ys)
    graph.plot([3], [50], marker='o', markersize=10, mfc='none', color='red')
    graph.grid()

    # Return initially created figure
    return fig