'''
Mock-45m
Workflow Timestamps
1. 1:30 Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
[2,7,9,3,1]

dp[2,7,11,10,12]

[2,7,9,3,1,8,3,2,1,4]

     2+9  2+9+1
      |     |    
[2,7,11,10,12,19,15,21,20,25]
dp[i] = max((nums[i]+dp[i-2]),(nums[i]+dp[i-3]))


[3,2,1,8,15,4,1,1]

dp[3,2,4,11,19,15]


2. Design a Solution / Template / Runtime and Space Complexity
Initialize a dp array of size nums. Add in first three houses sum.

for each house in range 3 -> n-1 we check for highest sum 
    dp[i] = max((nums[i]+dp[i-2]),(nums[i]+dp[i-3]))

return max(dp[-2:])
3. Write the Code And Pass Test Cases.
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        
        # Check if at least 3 houses, guaranteed 1
        if n < 3:
            return max(nums)
        # Add first three houses
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[0] + nums[2]
        
        # Traverse through houses adding up best route
        for i in range(3, n):
            dp[i] = max((nums[i]+dp[i-2]),(nums[i]+dp[i-3]))
            
        # Choose max of last two elements
        return max(dp[-2:])
