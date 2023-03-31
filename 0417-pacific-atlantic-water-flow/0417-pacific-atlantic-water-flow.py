'''
Mock-45m
Workflow Timestamps
1. 0:00 - 7:40 Make Sure You Understand the Problem
2. 7:40 - 25:30 Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
2. Design a Solution / Templete / Runtime and Space Complexity
BFS from the oceans inward, finding cells greater than current. 
Then the intersection of these two sets are the cells that can reach both oceans.

# helper bfs
def bfs(queue):
    reachable = set()
    
    while queue:
        r, c = q.get()
        
        reachable.add((r,c))
        
        directions = directions = [(1,0),(0,1),(-1,0),(0,-1)]
        new_r = r + d[0]
        new_c = r + d[1]
        if not in bounds
            continue
            
        if in reachable
            continue
        if new cell value < old cell value
            continue
            
        q.put(new_r, new_c)
        
    return reachable

pacific queue
atlantic queue
directions  

# Put left, right edge cells in queue
for i in range(rows):
    pacific_q.put(i, 0)
    atlantic_q.put(i, cols - 1)
    
# Put top, bottom edge cells in queue
for i in range(cols):
    pacific_q.put(0, i)
    atlantic_q.put(rows - 1, i)

pacific_cells = bfs(pacific_q)
atlantic_cells = bfs(atlantic_q)

return list(pacific_cells.intersection(atlantic_cells))
    

return output
3. Write the Code And Pass Test Cases.
'''
import queue



class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        if not heights or not heights[0]:
            return []
        
        pacific_q = queue.Queue()
        atlantic_q = queue.Queue()
        
        rows = len(heights)
        cols = len(heights[0])
        
        # Add left and right border cells
        for i in range(rows):
            pacific_q.put((i, 0))
            atlantic_q.put((i, cols - 1))
            
        # Add top and bottom border cells
        for i in range(cols):
            pacific_q.put((0, i))
            atlantic_q.put((rows - 1, i))  
            
        # Helper
        def bfs(queue):
            reachable = set()

            while not queue.empty():
                r, c = queue.get()

                reachable.add((r,c))

                for x, y in [(1,0),(0,1),(-1,0),(0,-1)]:
                
                    new_r = r + x
                    new_c = c + y

                    if rows <= new_r or new_r < 0 or cols <= new_c or new_c < 0:
                        continue

                    if (new_r, new_c) in reachable:
                        continue

                    if heights[new_r][new_c] < heights[r][c]:
                        continue

                    queue.put((new_r, new_c))

            return reachable
        
        pacific_cells = bfs(pacific_q)
        atlantic_cells = bfs(atlantic_q)
        
        return list(pacific_cells.intersection(atlantic_cells))
                        
                        
                        