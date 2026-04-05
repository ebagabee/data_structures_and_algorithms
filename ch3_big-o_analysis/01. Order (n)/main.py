def find_max(nums):
    if (len(nums) <= 0):
        return 0
    
    max_number = float('-inf')

    for num in nums:
        if num > max_number:
            max_number = num

    return max_number
