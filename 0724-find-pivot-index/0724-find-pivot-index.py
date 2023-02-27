'''
Workflow Timestamps
1. 0:00 - 3:00 Make Sure You Understand the Problem
2. 3:00 - 16:55 Design a Solution / Runtime and Space Complexity
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
[1] -> -1 

[0,0,0] -> 0
2. Design a Solution / Runtime and Space Complexity
Loop through nums. Starting with a left side sum of 0 and right side sum equal to total sum of nums.
Subtract current num from right sum and check if left = right
if left = right return that index 
else add current to left
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
# Pointers
left = 0
rigth = sum(nums)

for idx, num in enumerate(nums):
    
# Subtract current num from right sum and check if left = right
right -= num
if left == right:
    return idx

left += num 
4. Write the Code And Pass Test Cases.
'''
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Pointers
        left = 0
        right = sum(nums)

        for idx, num in enumerate(nums):

            # Subtract current num from right sum and check if left = right
            right -= num
            if left == right:
                return idx

            left += num 
        
        return -1
        
        
    