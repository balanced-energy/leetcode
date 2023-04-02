'''
Mock-45m
Workflow Timestamps
1. 2:00 Make Sure You Understand the Problem
2. 13:20 Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
n = 2
n = f(n+1)
[0,1,1,2]
1,1
2


n = 4
[0,1,1,2,3,5]
1,1,1,1
2,1,1
1,2,1
1,1,2
2,2

n = 5
f(n+1) = f(6) = 8 
[0,1,1,2,3,5,8]
1,1,1,1,1
1,1,1,2
1,1,2,1
1,2,1,1
2,1,1,1
2,2,1
1,2,2
2,1,2

2. Design a Solution / Templete / Runtime and Space Complexity
Initialize a dp array of size n + 1
set dp[0] = 0 and dp[1] = 1

for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]
    
return dp[n]
3. Write the Code And Pass Test Cases.
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+2)
        dp[0] = 0
        dp[1] = 1
        
        for i in range(2, n+2):
            dp[i] = dp[i-1] + dp[i-2]
    
        return dp[n+1]