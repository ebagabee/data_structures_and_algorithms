import math

def log_scale(data, base):
    log_array = []

    for item in data:
        log_array.append(round(math.log(item, base), 1))
    
    return log_array
