'''
Mock - 45m
Workflow Timestamps
1. 1:00 Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
[0,0,0]
[0,1,0]
[0,0,0]

dp
[1,1,1]
[1,0,1]
[1,1,2]

[0,1]
[0,0]

[1,1]
[1,1]

2. Design a Solution / Template / Runtime and Space Complexity
create dp array of mxn filled with 1's
rows = len(grid)
cols = len(grid[0])

for r in range(1, rows):
    for c in range(1, cols):
     if current cell is != 1 in grid
        if r-1 in grid != 1 and if c-1 in grid != 1:
            dp[r][c] = dp[r-1][c] + dp[r][c-1]
        elif r-1 in grid != 1:
            dp[r][c] = dp[r-1][c]
        elif c-1 in grid != 1:
            dp[r][c] += dp[r][c-1]
    
3. Write the Code And Pass Test Cases.

[0,0]
[1,1]
[0,0]

dp 
[1,1]
[0,0]
[0,0]
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        
        # Obstacle at end position
        if obstacleGrid[rows-1][cols-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        
        dp = [[0]*cols for _ in range(rows)]
        
        # Know starting position is not equal to obstacle already
        dp[0][0] = 1
        
        # Preprocess dp array accounting for obstacles
        for r in range(1, rows):
            if dp[r-1][0] == 1 and obstacleGrid[r][0] != 1:
                dp[r][0] = 1
                
        for c in range(cols):
            if dp[0][c-1] == 1 and obstacleGrid[0][c] != 1:
                dp[0][c] = 1
        
            
        for r in range(1, rows):
            for c in range(1, cols):
                if obstacleGrid[r][c] != 1:   
                    if obstacleGrid[r-1][c] != 1 and obstacleGrid[r][c-1] != 1:
                        dp[r][c] = dp[r-1][c] + dp[r][c-1]
                    elif obstacleGrid[r-1][c] != 1:
                        dp[r][c] += dp[r-1][c]
                    elif obstacleGrid[r][c-1] != 1:
                        dp[r][c] += dp[r][c-1]
                        
        return dp[rows-1][cols-1]