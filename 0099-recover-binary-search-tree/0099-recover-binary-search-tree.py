'''
Workflow Timestamps
1. 0:00 - 6:00 Make Sure You Understand the Problem
2. 6:00 - 20:55 Design a Solution / Runtime and Space Complexity
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem

         6
      5     9
          10  8
    
         6
      5     7
     8        4   
      
2. Design a Solution / Runtime and Space Complexity
Using inorder traversal, create a list. 

find_swapped will traverse list and check current i against the next value. 
first occurence of this we will store y = nums[i+1] and x = nums[i], second occurence we set y = nums[i+1] then break

recover function 
    if root then check if the value is equal to either of the swapped nodes.
        if it's equal to x, set the value to y, else set to x
        reduce count
        return when count is 0
    traverse tree recursively
    
runner code calling inorder
calling find_swapped
calling recover with count of 2

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
# inorder traversal function
return inorder(root.left) + [root.val] + inorder[root.right] if root else []

find_swapped 
traverse list and check current i against the next value. 
first occurence of this we will store y = nums[i+1] and x = nums[i], 
second occurence we set y = nums[i+1] then break


if root then check if the value is equal to either of the swapped nodes.
        if it's equal to x, set the value to y, else set to x
        reduce count
        return when count is 0
    traverse tree recursively
    
runner code calling inorder
calling find_swapped
calling recover with count of 2

4. Write the Code And Pass Test Cases.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Inorder traversal function
        def inorder_traversal(root):
            return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []
        
        # Find swapped nodes
        def find_swapped(nums):
            x = None
            y = None 
            
            n = len(nums)
            
            for i in range(n - 1):
                if nums[i + 1] < nums[i]:
                    y = nums[i+1]
                    
                    if x is None:
                        x = nums[i]
                    else:
                        break
            return x, y
        
        def recover(root, x, y, count):
            if root:
                if root.val == x or root.val == y:
                    if root.val == x:
                        root.val = y
                    else:
                        root.val = x
                    
                    count -= 1
                    if count ==  0:
                        return
                
                recover(root.left, x, y, count)
                recover(root.right, x, y, count)

        
        nums = inorder_traversal(root)
        x, y = find_swapped(nums)
        recover(root,x,y,2)
        