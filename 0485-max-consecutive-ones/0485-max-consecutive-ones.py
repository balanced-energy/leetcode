
'''
1. Make Sure You Understand the Problem
2. Design a Solution / Runtime and Space Complexity
- For loop through every num in nums. 
- Checking if current num is a 1, if it is increase count,
- else update max length if needed

Runtime: O(N)
Space: O(1)
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
max_count = 0
cur_count = 0

for each num
    if num is one
        increase count
    else 
        log length
        reset count

return one_count

4. Write the Code And Pass Test Cases.
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        cur_count = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                cur_count += 1
                
            else:
                max_count = max(max_count, cur_count)
                cur_count = 0
                
            # If last element is 1 update max
            if i == len(nums) - 1:
                max_count = max(max_count, cur_count)
        return max_count 
