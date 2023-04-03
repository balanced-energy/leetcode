'''
Mock - 45m
Workflow Timestamps
1. ~2:00 Make Sure You Understand the Problem
2. 9:30 Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem

[1,1,1]
[1,2,3]

[1,1,1,1,1,1,1]
[1,2,3,4,5,6,7]
[1,3,6,10,15,21,28]

dp[i] = dp[i-1][j] + dp[i][j-1]


2. Design a Solution / Template / Runtime and Space Complexity
# Initialize dp array of size mxn with 0's
dp = [[0]*n for _ in range(m)]

# Set first row and first column as 1's
for i in range(n):
    dp[0][i] = 1

for i in range(m):
    dp[i][0] = 1
    
# Starting at row 1, column 1 for 0 indexed cells
for i in range(1, m):
    for i in range(1,n):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

return dp[m][n]
    
3. Write the Code And Pass Test Cases.
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize dp array of size mxn with 0's
        dp = [[0]*n for _ in range(m)]

        # Set first row and first column as 1's
        for i in range(n):
            dp[0][i] = 1

        for i in range(m):
            dp[i][0] = 1

        # Starting at row 1, column 1 for 0 indexed cells
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]
