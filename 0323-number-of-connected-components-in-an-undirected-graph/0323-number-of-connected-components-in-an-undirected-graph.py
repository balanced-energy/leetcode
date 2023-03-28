'''
Mock-45m
Workflow Timestamps
1. 0:00 - 2:40 Make Sure You Understand the Problem
2. 2:50 - 15:55 Design a Solution / Runtime and Space Complexity
3. 15:55 - 24:35 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
Example 1: [[0,1],[1,2],[3,4]]
    adj list: 
    0:1
    1:2
    3:4

    0 -- 1
    |    
    3 -- 2      
    
    4 -- 5
    
    0: 1, 3
    1: 
    2: 
    3:2
    4:5
    
2. Design a Solution / Runtime and Space Complexity
Create adj list for nodes (undirected). For each node if not in visited, perform BFS adding all neighbors to visited. 
Increment component count after each bfs traversal.

3. Write a Template for Code in Logical Blocks. Aka Pseudocode


# BFS
def bfs(node, visited, adj_list):
q = queue()

q.put(node)

while(q):
cur = q.get()

visited.add(cur)

for neighbor in adj_list[cur]:
    q.put(neighbor)


visted = set()
components = 0

# Create adj list
adj_list = {}
for edge in edges:
    adj_list[edge[0]] = edge[1]
    

for node in range(n):
    if node not in visited:
        bfs(node, visited, adj_list)
        components += 1
    
    # Stop early if all nodes visited
    if len(visited) == n:
        return components  

    
4. Write the Code And Pass Test Cases.

    2 -- 3
    |   |
    1----      0
'''
import queue 

def bfs(node, visited, adj_list):
    q = queue.Queue()
    
    q.put(node)
    
    while not q.empty():
        cur = q.get()
        
        visited.add(cur)
        
        # Add all neighbors that haven't been visited to queue
        for neighbor in adj_list[cur]:
            if neighbor not in visited:
                q.put(neighbor)

    
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        components = 0
        adj_list = {}
        
        for node in range(n):
            adj_list[node] = []
            
        # Create adj_list
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
            
        for node in range(n):
            if node not in visited:
                bfs(node, visited, adj_list)
                components += 1
       
        return components