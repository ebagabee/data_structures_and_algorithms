# Insertion sort builds a sorted list on item at a time. Its much less efficient
# on large lists than merge because its O(n^2), but its actually faster
# (not in Big O terms, but due to smaller constants) than merge sort on small lists.

# For each index in the input list, starting with the second element:

# Set a j variable to the current index

# While j is greater than 0 and the elemtn at index j-1
# is greater than the element at index j:
    # 1. Swap the elements at indices j and j-1
    # 2. Decrement j by 1

# Return the list.

def insertion_sort(nums):
    for index in range(1, len(nums)):
        j = index
        
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
    return nums

        

    

    
        

