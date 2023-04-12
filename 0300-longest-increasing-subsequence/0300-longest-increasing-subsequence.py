'''
Mock - 45m
Workflow Timestamps
1. 1:45 Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.

1. Make Sure You Understand the Problem'
[0,1,3,2,3]
[1,2,3,3,4]

0,1,3
0,1,2,3


base case subsequence length 1

for num in nums:
    if next num < num
        continue
next num is strictly increasing
    add num to subsequence or not
    
else 
2. Design a Solution / Template / Runtime and Space Complexity

dp[i] = max(dp[i], dp[j] + 1)
3. Write the Code And Pass Test Cases.
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)