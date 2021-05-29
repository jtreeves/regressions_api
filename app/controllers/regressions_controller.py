from .regressions.get_regressions import get_regressions
from .regressions.post_regressions import post_regressions
from .regressions.put_regressions import put_regressions
from .regressions.delete_regressions import delete_regressions

regressions_controller = {
    'get_regressions': get_regressions,
    'post_regressions': post_regressions,
    'put_regressions': put_regressions,
    'delete_regressions': delete_regressions
}