import io
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg
from .images.create_linear_graph import create_linear_graph
from .images.create_quadratic_graph import create_quadratic_graph
from .images.create_cubic_graph import create_cubic_graph
from .images.create_hyperbolic_graph import create_hyperbolic_graph
from .images.create_exponential_graph import create_exponential_graph
from .images.create_logarithmic_graph import create_logarithmic_graph
from .images.create_logistic_graph import create_logistic_graph
from .images.create_sinusoidal_graph import create_sinusoidal_graph
from .images.create_root_graph import create_root_graph
from .images.create_maximum_graph import create_maximum_graph
from .images.create_minimum_graph import create_minimum_graph
from .images.create_inflection_graph import create_inflection_graph

def images_controller(source):
    def create_graph(source):
        if source == 'linear.png':
            return create_linear_graph()
        
        if source == 'quadratic.png':
            return create_quadratic_graph()
        
        if source == 'cubic.png':
            return create_cubic_graph()
        
        if source == 'hyperbolic.png':
            return create_hyperbolic_graph()
        
        if source == 'exponential.png':
            return create_exponential_graph()
        
        if source == 'logarithmic.png':
            return create_logarithmic_graph()
        
        if source == 'logistic.png':
            return create_logistic_graph()
        
        if source == 'sinusoidal.png':
            return create_sinusoidal_graph()
        
        if source == 'root.png':
            return create_root_graph()
        
        if source == 'maximum.png':
            return create_maximum_graph()
        
        if source == 'minimum.png':
            return create_minimum_graph()
        
        if source == 'inflection.png':
            return create_inflection_graph()

    fig = create_graph(source)
    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')