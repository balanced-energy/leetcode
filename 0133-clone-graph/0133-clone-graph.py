'''
Mock-45m
Workflow Timestamps
1. 0:00 - 2:45 Make Sure You Understand the Problem
2. 2:55 - 16:55 Design a Solution / Runtime and Space Complexity
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
2. Design a Solution / Runtime and Space Complexity
BFS from given node and if it's neighbor is unvisited then we clone the value to a new node
and add it to the visited map. 
If it's neighbor was already visited then we simply add the pointer to the visited node to 
our current nodes neighbors list.

3. Write a Template for Code in Logical Blocks. Aka Pseudocode

visited = {}

#bfs 
q = queue
q.put(Node(node.val, []))

while not q.empty():
    cur_node = q.get()
    
    for nbr in cur_node.neighbors:
        if nbr is not in visited:
            visited[nbr] = Node(nbr.val, [])
            q.put(visited[nbr])
        visited[cur_node].neighbors.append(visited[nbr])
        
return visited[cur_node]

    
4. Write the Code And Pass Test Cases.
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
import queue
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        visited = {}

        #bfs 
        q = queue.Queue()
        q.put(node)

        visited[node] = Node(node.val, []) 

        while not q.empty():
            cur_node = q.get()
            
            for nbr in cur_node.neighbors:
                if nbr not in visited:
                    visited[nbr] = Node(nbr.val, [])
                    q.put(nbr)
    
                visited[cur_node].neighbors.append(visited[nbr])
        
        return visited[node]
            
 