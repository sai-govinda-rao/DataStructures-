"""run the loop and compaire if element is equal to target element or not
if element target element return index
 else return element not found in the array"""
def Linear_Search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return f"Target Element Found at location:{i}"
        else:
            continue
    # it is for else block statement it Executes when loop run without taking break
    # otherwise it doesn't execute
    else:
        return "Element Not Found"


# taking list of inputs from user by space separated integers
space_separated_nums = input("Enter Numbers Separated By space:") # Enter integers which are separated by space
target = int(input("Enter Target Element:")) # enter target element which element location do you want to find
#convert "space_separated_nums" into list but still numbers are considered as strings
numbers = space_separated_nums.split(" ")
#so we will have to use type conversen
nums = []
for j in numbers:
    nums.append(int(j))
print(Linear_Search(nums, target))


"""
time complexity 
    best-case: O(1)
    average: O(n)
    worst-case: O(n)
"""
