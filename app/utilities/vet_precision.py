def vet_precision(precision):
    """ Ensure provided precision is a positive integer """
    
    # Return precision if precision meets criteria
    if isinstance(precision, int) and precision > 0:
        return precision
    
    # Return error if precision does not meet criteria
    else:
        return 'Precision must be a positive integer', 403