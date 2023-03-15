
'''
1. Make Sure You Understand the Problem

   1
 2 
        -> [1,2]

      1
   2     3
       4    5
      6    4   7    -> 
     8    6
   
max_height = -1,0,1,2
curr_height = 0,1,2,3
output = [-1, ]
                1
           2         3
         4   5     4     5
        6        7    6
       8  9  
     10
     

2. Design a Solution / Runtime and Space Complexity
Using reverse preorder traversal with right child accessed first. Has a height parameter and only appends children to ouput list when length of output list is equal to current level

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
return preorder(root, 0, [])

preorder(root, height, output):
    if root none:
        return
    
    if len(output) == height:
        output.append(root.val)
    
   
    preoder(root.right, height + 1, output)
    preorder(root.left, height + 1, output)
    
    return output

return right_side(root.right, output)
4. Write the Code And Pass Test Cases.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def preorder(root, height, output):
 
    if root is None:
        return 
    
    if len(output) == height:
        output.append(root.val)
    
   
    preorder(root.right, height + 1, output)
    preorder(root.left, height + 1, output)
    
    return output

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        return preorder(root, 0, [])
        
  