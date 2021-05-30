def vet_data_set(data_set):
    if data_set:
        if isinstance(data_set, list):
            for point in data_set:
                if isinstance(point, list):
                    for number in point:
                        if isinstance(number, (int, float)):
                            return data_set
                        
                        else:
                            return 'All numbers within coordinate pairs within data set must be integers or floats', 403
                
                else:
                    return 'Each coordinate pair within data set must be a list', 403
        
        else:
            return 'Data set must be a list', 403
    
    else:
        return 'Data set must be provided', 403