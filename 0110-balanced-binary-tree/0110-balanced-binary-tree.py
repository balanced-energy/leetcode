'''
Workflow Timestamps
1. 0:00 - 1:50 Make Sure You Understand the Problem
2. 2:00 - 24:20 Design a Solution / Runtime and Space Complexity
3. 24:20 - 28:55 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. 29:00 Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
[] -> true

     1
   2
 3         ->  false
2. Design a Solution / Runtime and Space Complexity
check if root is none, return True
Two height variables. left_height, right_height
Get heights of each subtree, then compare if difference is greater than 1 

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
# Main function 
if root is None:
    return True
    
left_height = helper(left)
right_height = helper(right)

if abs(left_height - right_height) > 1:
    return False

return True

# Helper

if root is None: return 0

return 1 + max(helper(left), helper(right))

4. Write the Code And Pass Test Cases.

           1
        2     2
     3           3
   4                4
            
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def max_depth(root):
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        left_height = max_depth(root.left)
        right_height = max_depth(root.right)
        
       
        if abs(left_height - right_height) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        