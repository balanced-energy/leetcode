# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def _inorder(root, arr):
    if root is None:
        return
    
    _inorder(root.left, arr)
    arr.append(root.val)
    _inorder(root.right, arr)
    
    return arr
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return _inorder(root, [])