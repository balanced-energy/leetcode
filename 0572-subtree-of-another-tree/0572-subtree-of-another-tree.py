
'''
1. Make Sure You Understand the Problem
 Tree  subtree
  1        1
2           -> true

  1       1
2   3   2
            -> false
2. Design a Solution / Runtime and Space Complexity
Check if current root is None. If it is then reached end of tree without finding subroot value so return false.
Else continue checking children of root until we find values equal, then call helper to confirm trees are equal or not


3. Write a Template for Code in Logical Blocks. Aka Pseudocode
if root is None return false

Check if root.val == subroot.val
If subroot has no children, return true
else 
    if equal_trees(root, subroot):
        return True

return isSubtree(root.right, subroot) or isSubtree(root.left, subroot)

# Helper
if root is None or subroot is None:
    if root is None and subroot is None:
        return True
    # One is None, one has a value
    else:
        return False
# Check values
if root.val != subroot.val:
    return False
# Calling on left and right 
return equal_tree(root.left, subroot.left) and equal_trees(root.right, subroot.right)

4. Write the Code And Pass Test Cases.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
 1   1
1   
'''
def equal_trees(root, subroot):
    if root is None or subroot is None:
        if root == subroot:
            return True
        else:
            return False

    if root.val != subroot.val:
        return False
    
    return equal_trees(root.left, subroot.left) and equal_trees(root.right, subroot.right)
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        if root.val == subRoot.val:
      
            if equal_trees(root, subRoot):
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        