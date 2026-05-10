'''
For each index:
    1. Set [smallest_idx] to the current index (of outer loop)
    2. For each index from [i + 1] to the end of the list:
        - If the number at the inner loop index is smaller than the number at [smallest_idx],
        set [smallest_idx] to the inner loop index.
    3. Swap the number at the outer loop index with the number at [smallest_idx]
    
Return the sorted list.

Assignment: Complete the selection_sort function.

It should sort the input list [nums] in ascending order using the selection sort algorithm.
The function should then return the sorted list.
'''

def selection_sort(nums):
    for i in range(len(nums)):
        smallest_idx = i
        
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[smallest_idx]:
                smallest_idx = j

        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]
    return nums