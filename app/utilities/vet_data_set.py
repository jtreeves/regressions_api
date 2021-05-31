def vet_data_set(data_set):
    if isinstance(data_set, list):
        for point in data_set:
            if isinstance(point, list):
                if len(point) is 2:
                    for number in point:
                        if isinstance(number, (int, float)):
                            pass
                        
                        else:
                            return 'All numbers within coordinate pairs within data set must be integers or floats', 403

                else:
                    return 'Each coordinate pair within data set must contain exactly 2 numbers', 403

            else:
                return 'Each coordinate pair within data set must be a list', 403
    
    else:
        return 'Data set must be a list', 403
    
    if len(data_set) >= 10:
        return data_set
    
    else:
        return 'Data set must contain at least 10 points', 403