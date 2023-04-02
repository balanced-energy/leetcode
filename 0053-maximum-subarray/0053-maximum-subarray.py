'''
Mock-45m
Workflow Timestamps
1. 1:15 Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem

2. Design a Solution / Templete / Runtime and Space Complexity
For each num we check if adding it to the current subarray creates a higher value or not
if adding num does help, we add it and compare that to our max subarray value
if it doesn't help we simply compare max subarray to current subarray 



3. Write the Code And Pass Test Cases.
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sub_array = nums[0] 
        max_sub_array = nums[0]

        for num in nums[1:]:
            cur_sub_array = max(num, cur_sub_array + num)
            max_sub_array = max(max_sub_array, cur_sub_array)
            
        return max_sub_array