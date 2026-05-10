# A is a unsorted list of integers (OK)

# If the length of A is less than 2, its already sorted so return it (OK)

# Split the input array into two halves down the middle (OK)

# Call merge_sort() twice, once on each half (OK)

# Return the result of calling merge(sorted_left_side, sorted_right_side) on
# thre results of the merge_sort() calls (OK)

def merge_sort(nums):
    if len(nums) < 2:
        return nums
    
    half_array = len(nums) // 2

    first_half, second_half = nums[:half_array], nums[half_array:]

    sorted_left_side = merge_sort(first_half)
    sorted_right_side = merge_sort(second_half)

    return merge(sorted_left_side, sorted_right_side)



# Inputs: A and B. Two Sorted lists of integers.

# Create a new final list of integers. 

# Set i and j equal to zero. They will be used to keep track of indexes in
# the input lists (A and B)

# Use a loop to compare the current elements of A and B
# If an element in A is less than or equal to its respective elements in B
# Add it to the final list and increment i
# Otherwise, add the item in B to the final list and increment j.
# Continue until all items from one of the lists have been added.

# After comparing all the items, there may be some items left over in either A or B
# Add those extra items to the final list.

# Return the final list.
def merge(first, second):
    final_list = []

    i = 0
    j = 0

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final_list.append(first[i])
            i += 1
        else:
            final_list.append(second[j])
            j += 1

    while i < len(first):
        final_list.append(first[i])
        i += 1

    while j < len(second):
        final_list.append(second[j])
        j += 1

    return final_list
        
