'''
Mock-45m
Workflow Timestamps
1. 0:00 - 3:50 Make Sure You Understand the Problem
2. 3:50 - 18:15 Design a Solution / Runtime and Space Complexity
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem

    0 1 2
    1 1 0
    2 1 0
    
1 min
    0 2 2
    2 1 0
    2 2 0
2 min
    0 2 2
    2 2 0
    2 2 0

2. Design a Solution / Runtime and Space Complexity
- Traverse cells, adding rotten oranges to queue and counting fresh oranges. 
    - Append(-1,-1) delimeter to queue
- using queue process rotten oranges adding delimeter (-1, -1) in our queue to track minute (levels). 
    Check if row == -1, increment minute and if queue add another delimeter
    
    else check 4 direction neighbors in bounds and if good orange, turn bad and decrement fresh oranges count
    
if fresh oranges != 0
    return -1

return minutes
    

- Add rotten oranges to bfs queue then, incrementing minute count in a tuple
return minute count from last orange added to visited 

3. Write a Template for Code in Logical Blocks. Aka Pseudocode


4. Write the Code And Pass Test Cases.
'''
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])

        fresh_oranges = 0
        minutes = -1
        directions = [(1,0), (-1, 0), (0,1), (0,-1)]


        for r in range(rows):
            for c in range(cols):
                # Add rotten oranges to queue
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        
        q.append((-1,-1))
        
        while q:
            row, col = q.popleft()
            
            if row == -1:
                minutes += 1
                
                if q:
                    q.append((-1,-1))
                    
            else:
                for d in directions:
                    row_nbr = row + d[0]
                    col_nbr = col + d[1]
                    if 0 <=  row_nbr < rows and 0 <= col_nbr < cols:
                        # check if good orange
                        if grid[row_nbr][col_nbr] == 1:
                            grid[row_nbr][col_nbr] = 2
                            fresh_oranges -= 1
                        
                            q.append((row_nbr, col_nbr))
                        
        # Not all oranges rotted
        if fresh_oranges != 0:
            return -1
        
        return minutes 
                    
            
            
            
            
            
            
            
            