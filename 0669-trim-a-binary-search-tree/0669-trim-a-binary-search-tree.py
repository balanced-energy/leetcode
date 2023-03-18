'''
Workflow Timestamps
1. 0:00 - 7:00 Make Sure You Understand the Problem
2. 7:Design a Solution / Runtime and Space Complexity
3. 26:00 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem

        6
     4      9 
   3   5   8
          7
      
      6
     5  7
    4
2. Design a Solution / Runtime and Space Complexity
if root is none, return none

if root value not within low and high ranges
   
    if root less than low return trimBST(root.right).
    else 
        trimbst(root.left)

root.left = trimBST on left
root.right = trimBST on right

return root

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
return _trim_bst(root, low, high)

#Helper
_trim_bst(root, low, high):
if root is none, return none
if root value not within low and high ranges

    if root less than low return trimBST(root.right).
    else 
        trimbst(root.left)

root.left = trimBST on left
root.right = trimBST on right

return root
    
4. Write the Code And Pass Test Cases.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def _trim_bst(root, low, high):
    if root is None:
        return None
    
    if root.val < low or root.val > high:
        # Need higher value so move right
        if root.val < low:
            #print(f'{root.val} < low')
            return _trim_bst(root.right, low, high)
        else:
            return _trim_bst(root.left, low, high)
        
    #print(f'root.left before{root.left}')  
    root.left = _trim_bst(root.left, low, high)
    #print(f'root.left after{root.left}')
    root.right = _trim_bst(root.right, low, high)

    return root

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        return _trim_bst(root, low, high)