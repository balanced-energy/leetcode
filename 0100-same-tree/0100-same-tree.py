'''
Workflow Timestamps
1. 0:00 - 2:40 Make Sure You Understand the Problem
2. 2:40 - 13:15 Design a Solution / Runtime and Space Complexity
3. 13:15 - 16:40 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. 16:40 - 20:10 Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
[] [] -> true

    1          1
  2   3     2    3  
4         4           -> false
2. Design a Solution / Runtime and Space Complexity
If root_a is none and  root_b is none return True. Else check root_a.val == root_b.val . if not return false
call function on children passing in opposite children to function

return isSameTree(root_A.left, root_B.left) and isSameTree(root_A.right, root_B.right)
 
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
# Base Case checks
if root_A is None and root_B is None:
    return True
elif root_A.val != root_B.val: 
    return False
    
return isSameTree(root_A.left, root_B.left) and isSameTree(root_A.right, root_B.right)
    
4. Write the Code And Pass Test Cases.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base cases
        if p is None or q is None:
            if p == q:
                return True
            else: 
                return False
        elif p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        