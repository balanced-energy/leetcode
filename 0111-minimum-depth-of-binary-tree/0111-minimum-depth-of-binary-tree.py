# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def _min_depth(root):
    if root is None:
        return 0
    if root.left is None:
        return _min_depth(root.right) + 1
    if root.right is None:
        return _min_depth(root.left) + 1
    
    return min(_min_depth(root.left), _min_depth(root.right)) + 1
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
       
        return _min_depth(root)
        