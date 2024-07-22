def Selection_Sort(nums):
    for i in range(len(nums)):
        temp = i   # store the i value in temporary variable

        for j in range(i+1, len(nums)):  # run another for loop from i+1
            if nums[temp] > nums[j]:  # check the condition
                # If condition is True then change the temp to j
                
                temp = j

        # after completing the 2nd for loop then we find the small element in the array
        # then swap nums[i] and nums[small element index which is temp]
        nums[i], nums[temp] = nums[temp], nums[i]
    return nums


# First of all we will take space separated numbers list from user
# Ex: 1 45 23 67 90 37.....etc.
# Map function is used to convert evey element to integer after split
nums = list(map(int, input("Enter numbers Separated by Space:").split()))

# call the Selection_sort Function and pass the parameter(nums)
result = Selection_Sort(nums)

# print the Sorted list(Which is returned by Selection_sort Function)
print(result)


"""

time complexity:
    best case: O(n^2)  
    average case: O(n^2)
    worst case: O(n^2)

"""