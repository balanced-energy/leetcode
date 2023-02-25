'''
Workflow Timestamps
1. 0:00 - 2:35 Make Sure You Understand the Problem
2. 2:35 - 6:40 Design a Solution / Runtime and Space Complexity
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
2. Design a Solution / Runtime and Space Complexity
Initialize a map to store nums:index 
Loop through all nums.
- Check if the target - current number is in map. 
    - If it is, return current index and target - current number as key to get value from map
- otherwise add number and index to map
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
# Initialize a map to store nums:index 
map = {}

for idx, num in enumerate(nums):
    if the target - num number in map. 
        return list with current index, and target - current number as key to get value from map
- otherwise add current number and index to map
4. Write the Code And Pass Test Cases.
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        
        for idx, num in enumerate(nums):
            # Found value such that value + num = target
            if target - num in nums_map:
                return [idx, nums_map[target-num]]
            # Add number and index to map
            else:
                nums_map[num] = idx