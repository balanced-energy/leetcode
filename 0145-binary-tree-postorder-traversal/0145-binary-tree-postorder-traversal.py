# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def _postorder(root, arr):
    if root is None:
        return 
    
    _postorder(root.left, arr)
    _postorder(root.right, arr)
    arr.append(root.val)
    
    return arr
    
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return _postorder(root, [])
        