def vet_data_set(data_set):
    """ Ensure provided data set meets necessary conditions """

    # Proceed if data set is a list
    if isinstance(data_set, list):
        for point in data_set:
            
            # Proceed if all elements of data sets are lists
            if isinstance(point, list):
                
                # Proceed if all elements of data sets contain only 2 elements
                if len(point) == 2:
                    for number in point:
                        
                        # Exit check if all elements of elements of data sets are numbers
                        if isinstance(number, (int, float)):
                            pass
                        
                        # Return error if any elements of elements of data set are not numbers
                        else:
                            return 'All numbers within coordinate pairs within data set must be integers or floats', 403

                # Return error if any elements of data set do not contain exactly 2 elements
                else:
                    return 'Each coordinate pair within data set must contain exactly 2 numbers', 403

            # Return error if any elements of data set are not lists
            else:
                return 'Each coordinate pair within data set must be a list', 403
    
    # Return error if data set not list
    else:
        return 'Data set must be a list', 403
    
    # Return data set if meets all criteria
    if len(data_set) >= 10:
        return data_set
    
    # Return error if data set not long enough
    else:
        return 'Data set must contain at least 10 points', 403