'''
Mock - 45m
Workflow Timestamps
1. Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.

1. Make Sure You Understand the Problem
        
         1
    -1       2 
  -1  15   3   4
                -4


left = 13
right = 9
root, left, right = 23

        -10 
      1     3
    2     3    4
                -1
                
    
left = 3
right = 10
max_path = (-7, 0, 3, 3, 10)
    left_sum = path_sum(root.left)
    right_sum = path_sum(root.right)
    max_path = max(root.val + left_sum, root.val + right_sum, root.val + left_sum + right_sum, left, right)


Do we include root?
Do we include left, right child?

2. Design a Solution / Template / Runtime and Space Complexity
- if root value + child subtree value is positive we include root in path
- 
max_path = 
if root is null:
    return 0
left_sum = path_sum(root.left)
right_sum = path_sum(root.right)
cur_max = max(root.val + left_sum, root.val + right_sum, root.val + left_sum + right_sum, left, right)
max_path = max(max_path, cur_max)

3. Write the Code And Pass Test Cases.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
    -2
  -1
'''

    

        
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path = float('-inf')
        
        def max_path_sum(root):
            if root is None:
                return 0

            left_sum = max(max_path_sum(root.left), 0)
            right_sum = max(max_path_sum(root.right), 0)

            cur_max = root.val + left_sum + right_sum

            self.max_path = max(self.max_path, cur_max)

            return root.val + max(left_sum, right_sum)
        
        max_path_sum(root)
        
        return self.max_path