'''
Mock-45m
Workflow Timestamps
1. 1:30 Make Sure You Understand the Problem
2. 19:00 Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
[1,5,3,7,8,2] = 1+3+7+2 vs 1+3+8

dp[12,14,11,9,8,2]

dp[i] = min((cost[i] + dp[i-1]), (cost[i] + dp[i-2]))



[1,3,3,6,8,2] = 3+6+2 vs 1+3+8

[1,3] -> 1 [3,3] -> 1+3
[1,3] -> 3 [3,6] -> 3+3

[1,3,3,6,8,2]

dp[12,11,11,8,8,2]

dp[i] = min((cost[i] + dp[i-1]), (cost[i] + dp[i-2]))


[1,3,3,6,8,2]

dp[1,3,0,0,0,0]
            
            1 + 3
            3 + 6
dp[i] = min((cost[i] + dp[i-1]), (cost[i] + dp[i-2]))


[1,3,3,6,8,2]

dp[12,11,11,8,8,2]


2. Design a Solution / Templete / Runtime and Space Complexity
Initialize dp array of size len costs - 2 with 0's and then append last two elements from cost array

# Traverse dp array in reverse starting from n-3 position
for i in range(len(dp) - 3, 1, -1):
    dp[i] = min((cost[i] + dp[i+1]), (cost[i] + dp[i+2]))

return min(dp[0], dp[1])

3. Write the Code And Pass Test Cases.
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Create array of 0's excluding last two steps
        n = len(cost)-2
        dp = [0]*n
        
        # Append last two steps
        dp.append(cost[-2])
        dp.append(cost[-1])
        
        # Traverse dp array in reverse order starting from n-3
        for i in range((len(cost) - 3), -1, -1):
            dp[i] = min((cost[i] + dp[i+1]), (cost[i] + dp[i+2]))

        return min(dp[0], dp[1])