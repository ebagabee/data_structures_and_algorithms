# Order Log N

def binary_search(target, arr):
    if len(arr) == 0:        
        return False
    
    low = 0
    high = len(arr) - 1

    while low <= high:
        median = (low + high) // 2

        if arr[median] == target:
            return True

        if arr[median] < target:
            low = median + 1
        
        if arr[median] > target:
            high = median - 1
        
    return False
    
