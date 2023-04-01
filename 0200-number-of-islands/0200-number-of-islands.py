'''
Mock-45m
Workflow Timestamps
1. 0:00 - 1:10 Make Sure You Understand the Problem
2. 1:15 - 13:10 Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
2. Design a Solution / Templete / Runtime and Space Complexity
Run bfs, adding connected land by checking 4-way direction.
Add cells to land set if connected from current cell. 


rows = len(grid)
cols = len(grid[0])
q = queue
visited = set()
islands = 0

def bfs(queue):
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    
    while not q.empty():
        r, c = q.get()
        
        visited.add((r,c))
        
        # Checks 4 way adjacent cells
        for x, y in directions:
            new_r = r + x
            new_c = c + y
            
            # Check for adjacent land
            if new coordinates in bounds and = 1 and not in visited
                add to queue
            
for r in len(rows):
    for c in len(cols):
        if ((r,c)) not in visited and == 1:
            q.put((r,c))
            islands += 1
            bfs(q)

return islands
    
3. Write the Code And Pass Test Cases.
'''
import queue
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = queue.Queue()
        islands = 0

        def bfs(queue):
            directions = [(1,0), (0,1), (-1,0), (0,-1)]

            while not queue.empty():
                r, c = queue.get()

                # Checks 4 way adjacent cells
                for x, y in directions:
                    new_r = r + x
                    new_c = c + y

                    # Check for adjacent land
                    if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols:
                        continue
                        
                    if grid[new_r][new_c] == "1":
                        queue.put((new_r, new_c))
                        grid[new_r][new_c] = '0'
        
        # Visit every cell                
        for r in range(rows):
            for c in range(cols):
                # If not visited and is land perform bfs
                if grid[r][c] == "1":
                    q.put((r,c))
                    grid[r][c] = '0'
                    islands += 1
                    bfs(q)

        return islands