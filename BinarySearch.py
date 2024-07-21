def Binary_Search(nums, lb, ub):
    while lb <= ub:  # loop continue till condition satisfies
        # calculate the mid value
        mid = (lb + ub) // 2

        # check if mid is equals to target then print target found at mid
        if nums[mid] == target:
            return f"Target Element Fond at Index: {mid}"

        # in case nums[mid] less than target -> then modify lower-bound = mid+1
        elif nums[mid] < target:
            lb = mid+1

        # in case nums[mid] grater than target -> then modify upper-bound = mid-1
        else:
            ub = mid-1

    # if loop end without return anything then execute else block
    else:
        return f"Target Not Found(It means target element is not in the array"


# taken input from user Which are separated by space
# using map function to convert string to integer in every element 
nums = list(map(int, input("Enter space separeted numbers:").split()))

# target Element taken from user
target = int(input("Enter Target Element:"))

# set lower-bound and upper-bound
lb = 0  # lower bound
# index starts from 0 so we set lb = 0

ub = len(nums)-1  # upper bound
# index ends to length of array-1 that's why we set ub = length of array-1

# The Major drawback in binary search is we must give elements in order
# call the Function and pass The parameters
result = Binary_Search(nums, lb, ub)
print(result)
