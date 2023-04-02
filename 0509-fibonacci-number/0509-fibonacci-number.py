'''
Mock-45m
Workflow Timestamps
1. 1:45 Make Sure You Understand the Problem
2. 8:45 Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
n = 3
dp [0,1,1,2]
dp[i] = dp[i-1] + dp[i-2]


n = 5
dp[0,1,1,2,3,5,8]


n = 4
dp[0,1,1,2,3]
2. Design a Solution / Templete / Runtime and Space Complexity
Use dynamic programming. Create a dp array of size n+1 with 0,1 as first elements.

dp = 0 * n+1
dp[0] = 0
dp[1] = 1

for i in range(2, n):
    dp[i] = dp[i-1] + dp[i-2]

return dp[n]

n = 2

dp[0,1,0]
3. Write the Code And Pass Test Cases.
'''
class Solution:
    def fib(self, n: int) -> int:
        
        dp = [0]*(n+2)
        dp[0] = 0
        dp[1] = 1
        
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]
        