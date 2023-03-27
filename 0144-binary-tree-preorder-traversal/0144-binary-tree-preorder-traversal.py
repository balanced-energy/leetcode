# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def _preorder(root, arr):
    if root is None:
        return
    
    arr.append(root.val)
    _preorder(root.left, arr)
    _preorder(root.right, arr)
    
    return arr
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return _preorder(root, [])
        