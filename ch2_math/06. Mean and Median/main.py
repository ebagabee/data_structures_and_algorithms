def average_followers(nums):
    if len(nums) < 1:
        return None
    
    sum_of_nums = 0

    for num in nums:
        sum_of_nums += num

    return sum_of_nums / len(nums)
