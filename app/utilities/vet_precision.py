def vet_precision(precision):
    if isinstance(precision, int) and precision > 0:
        return precision
    
    else:
        return 'Precision must be a positive integer', 403