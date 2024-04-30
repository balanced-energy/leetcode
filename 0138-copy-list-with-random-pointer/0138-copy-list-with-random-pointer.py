'''
6:00 Understand the problem
[] -> []

[[1,None]] 

[[1, 0]]

[[1,1],[2,1]] 
{(1),(2)}
[[1,1],[2,1]]

              h
[[1,2],[2,0],[3,None]]
{(1),(2),(3)}
[[1,2]>[2,0]>[3,None]>None]


[[1,None], [2,None],[3,None]]


  
[[7,null],[13,0],[11,4],[10,2],[1,0]]


28:00 Design a solution
- We want to create a new node based on current nodes value in input list. 
- Set next pointer
- Set random pointer 

- Using a set track nodes that are created or not

    - Setting pointers could lead to pointing to a node that isn't created yet 


recursive function 
    - base case when node is None
    - if node is already in set, return node 
    
    - create the node with curr nodes value
    - add to created set
    
    -  new_node.next = recursive_cal(head.next)
    -  new_node.random = recursive_cal(head.random)
    
    -  return new_node

Runtime: O(N)
Space: O(N)
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.visited = {}
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        
        # Check set for head 
        if head in self.visited:
            return self.visited[head]
        
        # Create new node with head value and add to set
        new_node = Node(head.val)
        
        self.visited[head] = new_node
        
        new_node.next = self.copyRandomList(head.next)
        new_node.random = self.copyRandomList(head.random)
        
        return new_node 
        