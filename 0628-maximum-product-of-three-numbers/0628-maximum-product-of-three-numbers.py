'''
Workflow Timestamps
1. 0:00 - 2:15 Make Sure You Understand the Problem
2. 2:15 - 4:00 Design a Solution / Runtime and Space Complexity
3. 4:00 - Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem

nums = [1,4,3,6,-7,-8]
2. Design a Solution / Runtime and Space Complexity
 # Attempt #1
 Get 5 numbers, 2 by calling min() 3 by calling max()
 Identify if we will use two negative values
        if both are greater second_max number 
            then append both negatives and first max
        else append all three max() nums 
Then multiply values.

Calculate first 
# Attempt #2
while end < len(nums):
window of size 3
calculate product 
compare it to max_product, store max of the two


Runtime: O(N)
Space: O(1)
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
create max_nums list


    first min 
    second min
    first max
    second max
    third max 
    If both mins are greater than second max
        add both and second max to max_nums
    
    add to list 
    remove cur_max from nums

# Second attempt 

# Initialize pointers 
start = 0
# We know at least 3 nums 
end = 2
max_product = -inf

while end < len(nums):
    calculate product
    compare to previous saved max and update if needed

return max_product
# Calculate product
return max_nums[0] * max_nums[1] * max_nums[2]

4. Write the Code And Pass Test Cases.
'''

'''
[-1, -2, 1, 4]

'''
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # If three elements return all three
        if len(nums) == 3:
            return nums[0]*nums[1]*nums[2]
        
        # Get max minimum numbers 
        min_first = nums.pop(nums.index(min(nums)))
        min_second = min(nums)
        
        # Get max numbers
        max_first = nums.pop(nums.index(max(nums)))
        max_second = nums.pop(nums.index(max(nums)))
        max_third = nums.pop(nums.index(max(nums)))
        
        # Checks if we use greatest two negatives values
        print(f'min1:{min_first}, min2:{min_second}, max1:{max_first}, max2:{max_second}, max3:{max_third}')
        if min_first * min_second * max_first > max_first * max_second * max_third:
                return min_first * min_second * max_first
        
        # Return product
        return max_first * max_second * max_third


        