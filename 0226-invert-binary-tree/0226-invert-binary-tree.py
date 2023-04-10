'''
Workflow Timestamps
1. 0:00 - 2:45 Make Sure You Understand the Problem
2. 2:45 - 9:13 Design a Solution / Runtime and Space Complexity
3. 9:13 - 13:30 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. 13:30 - 22:04 Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem

  1               1 
2   3           3   2
      4   ->  4
2. Design a Solution / Runtime and Space Complexity
Base case: if root is none, return. 
Otherwise check if both left and right child exists swap left and right children. 
If only one exists, set it as opposite child of current root.
ex. if right exists and left child doesn't, set right as left child 
call invertTree on children 

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
# Base case
if root is None return

# Create helper function
_invert() 
# Check if both children exist
if root.left and root.right
    swap children
   
elif if root.right
    set right as left child
    
else
    set left as right child
    
invertTree(right)
invertTree(left)

return root
4. Write the Code And Pass Test Cases.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
  1       1
2    ->     2
'''
def _invert_tree(root):
    # Base Case
    if root is None:
        return 
    
    # # Check if both children exist
    # if root.right and root.left:
    #     # Store right child pointer
    #     right_child = root.right
    #     root.right = root.left
    #     root.left = right_child
    # elif root.right:
    #     root.left = root.right
    #     root.right = None
    # else:
    #     root.right = root.left
    #     root.left = None
    temp = root.right
    root.right = root.left
    root.left = temp
    
    # Call on children
    _invert_tree(root.right)
    _invert_tree(root.left)
    
    return root
    
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return _invert_tree(root)
        