
'''
1. Make Sure You Understand the Problem
         1
      2      3
    4   5  6   7
   8        9        p = 6  q = 5

parents = {1:None, 2:1, 3:1, 4:2, 5:2, 6:3 }
q = [ (6,3), (7,3)]
2. Design a Solution / Runtime and Space Complexity
Use a hashmap that stores node:parent associations

Then traverse tree while p and q are not in hash map and add nodes children:parent values to map 
Once they both are in map
we add p and it's parents to a set, then check if q in set, if not set q to it's parent until reaches root

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
# map of node:parent
parents = {root:None}

stack = [root]

while p not in parents and q not in parents:
    node = stack.pop()
    
    if left child add to stack with (child.val, node.val)
    if right child add to stack with (child.val, node.val)

# We know p or q is in map with parent values
# add p and it's parents to a set
while p:
    add p to set
    p = parents[p]

# Check for LCA in p's ancestors
while q not in ancestors:
    q = parents[q]

return q
4. Write the Code And Pass Test Cases.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = {root:None}
        
        stack = [root]
        
        while p not in parents or q not in parents:
            node = stack.pop()
            
            # Add (children,parent) to queue 
            if node.left:
                parents[node.left] = node
                stack.append(node.left)
            if node.right:
                parents[node.right] = node
                stack.append(node.right)
        
        # Create ancestors set for p
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parents[p]

        # Check for LCA between q and p
        while q not in ancestors:
            q = parents[q]
    
        return q