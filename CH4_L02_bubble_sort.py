def bubble_sort(nums):
    swapping = True

    end = len(nums)

    while swapping:
        swapping = False

        for i in range(1,end):
            if nums[i - 1] > nums[i]:
                swapping = True

                temp = nums[i - 1]

                nums[i - 1] = nums[i]
                nums[i] = temp

        end -= 1

    return nums