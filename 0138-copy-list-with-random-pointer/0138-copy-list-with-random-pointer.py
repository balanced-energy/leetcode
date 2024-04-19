'''
4:15 Understand the problem
[] -> []

[[1,0]] -> [[1,0]]

[[1,null]] -> [[1,null]]

[[1,1],[2,1]] -> [[1,1],[2,1]]

[[3,null],[3,0],[3,null]] -> [[3,null],[3,0],[3,null]]

[[1,2],[2,0],[3,1]] -> [[1,2],[2,0],[3,1]]


29:00 Design a solution

- visited map old_node:new_node  
- recursive function input of head
    - if head is None: return None
    - if node in visited
        return visited[head]
     
    - create new node
    - add it to visited 
    - new_node.next = func(head.next)
    - new_node.random = func(head.random)
    
    return node

{old_node(1):new_node(1), 2:2}
[[1,1],[2,1]]

{1:1}
[[1,0]] -> [[1,0]]

{7:7, 13:13, 11:11, 10:10, 1:1}
     
[[7,null],[13,0],[11,4],[10,2],[1,0]]

{1:1,2:2,3:3 }
[[1,2],[2,0],[3,1]] 


Runtime: O(N)
Space: O(N)
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        self.visited = {}
        return self.copy_node(head)
        
    def copy_node(self, head):
        if head == None:
            return None

        if head in self.visited:
            return self.visited[head]

        node = Node(head.val, None, None)
        self.visited[head] = node 

        # Recursively call on head.next and head.random
        node.next = self.copy_node(head.next)
        node.random = self.copy_node(head.random)

        return node

        