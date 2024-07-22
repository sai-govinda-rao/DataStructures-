def Insertion_Sort(nums):
    for i in range(1, len(nums)):  # run the loop from 1st index
        temp = nums[i]  # set nums[i] as a temporary variable
        j = i-1
        while j >= 0 and nums[j] > temp:
            # while loop run if both conditions satisfies
            # 1st one j grater than or Equals to 0
            # 2nd one nums[j] is grater than temporary variable

            nums[j+1] = nums[j]  # then swapping happens
            # here we can swap only one element

            j -= 1  # finally decrement the j value

        # after completing the while loop temp will store nums[j+1]
        nums[j+1] = temp
    return nums

# First of all we will take space separated numbers list from user
# Ex: 1 45 23 67 90 37.....etc.
# Map function is used to convert evey element to integer after split
nums = list(map(int, input("Enter numbers Separated by Space:").split()))

# call the Insertion_sort Function and pass the parameter(nums)
result = Insertion_Sort(nums)

# print the Sorted list(Which is returned by Insertion_sort Function)
print(result)
