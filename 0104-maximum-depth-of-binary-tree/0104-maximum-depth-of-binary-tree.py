'''
Workflow Timestamps
1. 0:00 - 1:50 Make Sure You Understand the Problem
2. 1:50 - 4:55 Design a Solution / Runtime and Space Complexity
3. 4:55 - 6:05 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem

[] -> 0
 
  1
2   3
      4   -> 3 
      
      
2. Design a Solution / Runtime and Space Complexity
Recursively add up nodes down the tree.

Base Case: If root is none: return 0
Return 1 + max of calling max_depth on each child node

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
# Base case

if root is None:
    return 0

return 1 + max(max_depth(left child), max_depth(rigth child))

4. Write the Code And Pass Test Cases.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def max_depth(root):
     # Base case 
        if root is None:
            return 0
        
        return 1 + max(max_depth(root.left), max_depth(root.right))
        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return max_depth(root)
       
    