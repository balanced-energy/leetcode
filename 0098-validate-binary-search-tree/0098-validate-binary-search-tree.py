'''
Workflow Timestamps
1. 0:00 - 1:15 Make Sure You Understand the Problem
2. 1:15 - 5:20 Design a Solution / Runtime and Space Complexity
3. 5:20 - 7:20 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. 7:20 - 11:44 Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
2. Design a Solution / Runtime and Space Complexity
Helper function that takes in min and max values. min and max start at negative and positive infinity
if root is none return true
These track the subtrees valid ranges when we call on left and right childred.
if root not within range, return false. Continue to call function on children with root.val set as max when
traversing to the left, and root.val set as min when traversing to the right. 
return true

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
# main
    return _invalid_bst(root, -inf, inf)
# helper
_invalid_bst(root, min, max)
    if root is none return true
    
    check root is within range
    if not return false
    
    if not call on left with root as max 
    if not call on right with root as min
    
    return true
    
4. Write the Code And Pass Test Cases.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def _invalid_bst(root, min_val, max_val):
    if root is None:
        return True
    
    if root.val <= min_val or root.val >= max_val:
        return False
    
    if not _invalid_bst(root.left, min_val, root.val):
        return False
    
    if not _invalid_bst(root.right, root.val, max_val):
        return False
    
    return True
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return _invalid_bst(root, float(-inf), float(inf))
        