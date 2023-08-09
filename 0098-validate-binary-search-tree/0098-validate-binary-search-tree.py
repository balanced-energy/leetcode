# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Call helper function passing in -inf and inf as min, max values
Create helper function with signature valid_bst(root, min, max)
    Base case will be if root null 
        Return True
    Then check if root is within our given range
        min <= root <= max
        If not within range return False
    Return call to helper from left child 
        Left child means we need the new max to be our root
        valid_bst(root.left, min, root)
    AND 
    Return call to helper from right child
        Right child means we need new min to be our root
        valid_bst(root.right, root, max)

'''
def valid_bst(root, minimum, maximum):
    if root is None:
        return True
    
    if not minimum < root.val < maximum:
        return False
    
    return valid_bst(root.left, minimum, root.val) and valid_bst(root.right, root.val, maximum)
    
    
    
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return valid_bst(root, -inf, inf)
        