'''
Note: Daughter is watching a show so I'm continue to try and type thoughts out. 

Workflow Timestamps
1. 0:00 - 1:40 Make Sure You Understand the Problem
2. 1:40 - 3:30 Design a Solution / Runtime and Space Complexity
3. 3:30 - 6:00 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. 6:00 - Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
At least one num, otherwise check for duplicates
nums = [1,2,3,1]
set = (1,2,3) found in map return true

nums = [1] = False 
set = (1) return False

2. Design a Solution / Runtime and Space Complexity
Traverse through each element adding to set checking if in set. If found return True, else can return false.

Runtime: O(N) - Traverse through each element once
Space: O(N) - Wonder if way to do with constant space?

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
# Initialize set()
seen = set()
for i in nums:
    if i in seen:
        return True 
    seen.add(i)
    
return False
4. Write the Code And Pass Test Cases.
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Initialize seen set
        seen = set()
        
        # Add each number to set and check if already has been seen
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        
        return False
        