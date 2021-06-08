import io
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg
from .images.create_random_graph import create_random_graph
from .images.create_sin_graph import create_sin_graph

def images_controller(source):
    def create_figure(source):
        if source == 'sin.png':
            return create_sin_graph()
        
        if source == 'random.png':
            return create_random_graph()

    fig = create_figure(source)
    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')