from app.middleware.current import current_regression

def get_regressions():
    return current_regression(), 200