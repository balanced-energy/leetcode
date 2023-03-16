'''
Workflow Timestamps
1. 0:00 - 2:05 Make Sure You Understand the Problem
2. 2:05 - 15:30 Design a Solution / Runtime and Space Complexity
3. 15:30 - 20:30 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
[] val = 1 -> [1]


2. Design a Solution / Runtime and Space Complexity
Check if root is none. If it is return new tree node with val
Traverse down tree comparing val to current node moving left or right and tracking parent node and direction 
until we reach an empty node. Then we know are in corrent location and set val to child of parent and direction

# In spot where to add value
set parent and proper child left or right

return root 

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
if not root:
    return TreeNode(val)

node = root
is_right = None
    
while node is not none
    set parent as  node
    
    if val is less than node
        is_right = False
        set node to left child
    
    else 
        is_right = True
        set node to right child 

# We are in proper spot to add node
if is_right:
    parent.right = TreeNode(val)
else:
     parent.left = TreeNode(val)
     
 return root
4. Write the Code And Pass Test Cases.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        node = root
        is_right = None
        
        # Find position to add new value 
        while node:
            parent = node
            
            if val < node.val:
                is_right = False
                node = node.left
            else:
                is_right = True
                node = node.right
        
        # We are in corrent spot to create new value
        if is_right:
            parent.right = TreeNode(val)
        else:
            parent.left = TreeNode(val)
            
        return root