# Quick sort is an efficient sorting algorithm thats widely used in production
# sorting implementations. Like merge sort, quick sort is recursive
# divide and conquer algorithm.

# --- Divide ---
# Select a pivot element that will preferably end up close to the center
# of the sorted pack

# Move everything onto the "greater than" ou "less than" side of the pivot

# The pivot is now in its final position

# Recursively repeat the operation on both sides of the pivot

# --- Conquer ---
# The array is sorted after all elements have been through the pivot operation

# --------------------
# - Select a pivot element, Well arbitrarily choose the last element in the list

# - Move through all the elements in the list and swap them around until all the numbers
# less than the pivot are on the left, and the numbers greater than the pivot are on the right

# - Move the pivot between the two sections where it belongs

# - Recursively repeat for both sections

# Assignment:

# We now have two sorting algorithms on our LockedIn backend!
# It is a bit annoying to maintain both in the codebase.
# Quicksort is fast on large datasets just like merge sort
# but is also lighter on memory usage. 
# Lets use quick sort for both follower count and influencer revenue sorting

# Complete the quick_sort and partition functions according to the given algorithms.

# The Process is started with quick_sort(A, 0, len(A) - 1)

# [ ] Complete quick_sort(nums, low, high):
    # [ ] If low is less than high:
        # [ ] Partition the input list using the partition function and store
            # The returned middle index
        # [ ] Recursively call quick_sort on the elements right of the pivot
            # (low to middle - 1)
        # [ ] Recursively call quick_sort on the elements right of the pivot
            # (middle + 1 to high)

# [ ] partition(nums, low, high)
    # [ ] Set pivot to the element at index high
    # [ ] Set i to the index before low
    # [ ] For reach index (j) in range(low, high):
        # [ ] If the element at index j is less than the pivot:
            # [ ] Increment i by 1
            # [ ] Swap the element at index i with the element at index j
    # [ ] Swap the element at index i + 1 with the element at index high
        # (the pivots position)
    # [ ] Return i + 1 (the pivots new index)

def quick_sort(nums, low, high):
    if low < high:
        middle = partition(nums, low, high)

        quick_sort(nums, low, middle - 1)
        quick_sort(nums, middle + 1, high)


def partition(nums, low, high):
    pass