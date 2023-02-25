'''
Workflow Timestamps
1. 0:00 - 3:15 Make Sure You Understand the Problem
2. 3:15 - 11:10 Design a Solution / Runtime and Space Complexity
3. 11:10 - 41:24 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
[2,3,0,2,1] = True

[3,2,2,0,1,1,1] = True

[3,1,2,0,4]
2. Design a Solution / Runtime and Space Complexity
Loop through all nums
Store a best index value that is the current element plus it's index. 
if we find an element greater than our best index return false
else update best index 

Runtime: O(N)
Space:(1)

3. Write a Template for Code in Logical Blocks. Aka Pseudocode

best_index = 0

# Loop through nums
for num in nums:
    if num > best_index:
        return False
    else
        update best index 

4. Write the Code And Pass Test Cases.

[1,1,4,1]
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        best_index = 0
        
        for idx, num in enumerate(nums):
            if idx > best_index:
                return False
            best_index = max(best_index, nums[idx] + idx)
        return True