def vet_precision(precision):
    if precision:
        if isinstance(precision, int) and precision > 0:
            return precision
        else:
            return 'Precision must be a positive integer', 403
    else:
        return 'Precision must be provided', 403