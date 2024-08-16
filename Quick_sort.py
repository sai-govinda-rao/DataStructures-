# Quick Sort
# Partition Function which will set the pivot element in the correct place in each call
def Partition(nums, start, end):
    pivot_index = start
    pivot_element = nums[pivot_index]
    while start < end:
        while start < len(nums) and nums[start] <= pivot_element:
            start += 1
        while nums[end] > pivot_element:
            end -= 1
        if start < end:
            # if condition satisfies swap the elements
            nums[start], nums[end] = nums[end], nums[start]
    # after successfully loop completed then swap pivot index and end
    nums[pivot_index], nums[end] = nums[end], nums[pivot_index]

    # finally end is the correct location of pivot element then return it
    return end

def Quick_sort(nums, start, end):
    if start < end:
        loc = Partition(nums, start, end)
        # Partition function return the correct location of the pivot element
        # then again call the Quick sort function from start to loc-1
        # and loc+1 to end
        # quick sort is divide and sorting technique

        Quick_sort(nums, start, loc-1)
        Quick_sort(nums, loc+1, end)
    return nums
# Taking Space separated integers from users
nums = list(map(int, input("Enter Space separated Integers:").split(" ")))

# call The Quick_sort function and pass the numbers list and starting index, ending index
print(Quick_sort(nums, 0, len(nums)-1))





# Quick sorting algorithm in side of the class

class Solution():
    def Partition(self, nums, start, end):
        pivot_index = start
        pivot_element = nums[pivot_index]
        while start < end:
            while start < len(nums) and nums[start] <= pivot_element:
                start += 1
            while nums[end] > pivot_element:
                end -= 1
            if start < end:
                nums[start], nums[end] = nums[end], nums[start]
        nums[pivot_index], nums[end] = nums[end], nums[pivot_index]
        return end
    def Quick_sort(self, nums, start, end):
        if start < end:
            loc = Solution().Partition(nums, start, end)
            Solution().Quick_sort(nums, start, loc-1)
            Solution().Quick_sort(nums, loc+1, end)
        return nums
nums = [10, 14, 1, 30, 56, 5, 9, 56, 20]
a = Solution().Quick_sort(nums, 0, len(nums)-1)
print(a)
