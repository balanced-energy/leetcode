'''
Mock - 45m
Workflow Timestamps
1. Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.

1. Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity

Traverse cells checking for cell hasn't been seen and if value of 1 
passing into bfs function if value of 1
bfs has a queue, and checks 4 directionally for other cells with value of 1
if adjacent cell has a value of 1, add to queue
return total area

seen = set()
max_area = 0
for row 
    for col
    if (r,c) not in seen and grid[r][c] == 1:
        total_area = bfs(row, col)
        max_area = max(max_area, total_area)
        
    return max_area

def bfs(row, col):
    q = queue.Queue()
    area = 0
    
    while not q.empty():
        add (row,col) to seen 
        check cells neighbors in all directions
        if valid neighbors and has a value of 1 
            add to queue
            increment area 
    return area
3. Write the Code And Pass Test Cases.


[1,1,0,0,0]
[1,1,0,0,0]
[0,0,0,1,1]
[0,0,0,1,1]
'''
import queue 
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        seen = set()
        max_area = 0
        
        def bfs(row, col):
            area = 1
            directions = [(1,0), (0,1), (-1,0), (0,-1)]
            q = queue.Queue()
            q.put((row,col))
           
            while q.qsize() > 0:
                queue_size = q.qsize()
                cur_r, cur_c = q.get()
                 
                
                # check cells neighbors in all directions
                for x, y in directions:
                    # Valid indices
                    if (cur_r + x, cur_c + y) not in seen:
                        if 0 <= cur_r + x and cur_r + x < ROWS and 0 <= cur_c + y and cur_c + y < COLS:
                            if grid[cur_r + x][cur_c + y] == 1:
                                q.put((cur_r + x, cur_c + y))
                                seen.add((cur_r + x,cur_c + y))
                                area += 1
            return area
        
        
        # Traverse all cells
        for r in range(ROWS):
            for c in range(COLS):
                # Check for land and get area
                if (r,c) not in seen and grid[r][c] == 1:
                    seen.add((r,c))
                    cur_area = bfs(r, c)
                    max_area = max(max_area, cur_area)

        return max_area