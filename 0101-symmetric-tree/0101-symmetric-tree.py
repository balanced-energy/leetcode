# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def _symmetric(left, right):
    if left is None or right is None:
            return left == right 
        
    if left.val != right.val:
            return False
    
    return _symmetric(left.left, right.right) and _symmetric(left.right, right.left)


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return _symmetric(root.left, root.right)
  