def Bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1-i):   # This Second loop performs sorting technique
            if nums[j] > nums[j+1]:  # If this condition is true then Swapping happens

                # if you want ascending order of our numbers then use nums[j] > nums[j+1]
                # if you want descending order of our numbers then use nums[j] < nums[j+1]
                nums[j], nums[j+1] = nums[j+1], nums[j]

    # after completing the two loops. our nums are in either Ascending or descending order
    # which is depending on our condition
    return nums


# First of all we will take space separated numbers list from user
# Ex: 1 45 23 67 90 37.....etc.
# Map function is used to convert evey element to integer after split
nums = list(map(int, input("Enter numbers Separated by Space:").split()))

# call the Bubble_sort Function and pass the parameter(nums)
result = Bubble_sort(nums)

# print the Sorted list(Which is returned by Bubble_sort Function)
print(result)


"""

time complexity:
    best case: O(n)   # If array is already sorted
    average case: O(n^2)
    worst case: O(n^2)

"""